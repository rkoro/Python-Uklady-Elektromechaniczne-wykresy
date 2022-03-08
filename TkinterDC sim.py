#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)

####################################################################
# MACIERZE STANU SILNIKA DC                                        #
#               _______A_______   __X__   ______B______   __U__    #
#               |             |   |   |   |           |   |   |    #
#       -- --   --           --   -- --   --         --   -- --    #
#   d   | i |   | -R/L  -Kv/L |   | i |   | 1/L    0  |   | V |    #
#  -- * |   | = |             | * |   | + |           | * |   |    #
#  dt   | w |   | Kt/J   -F/J |   | w |   |  0   -1/J |   | T |    #
#       -- --   --           --   -- --   --         --   -- --    #
####################################################################

###########################################################
# ABSTRAKT KLAS:                                          #
#     class OBIEKT(OBJECT):                               #
#                                                         #
#         INICJACJA                                       #
#         def __init__(self, real):                       #
#             self.ins                                    #
#             self.out                                    #
#                                                         #
#         OBLICZENIE NASTEPNEJ PROBKI                     #
#         def next_S(self):                               #
#                                                         #
#                                                         #
#         USTAWIENIE WEJSC                                #
#         def set_INS(self, real)                         #
#                                                         #
#                                                         #
#         ODCZYT WYJSC                                    #
#         def get_OUTP(self):                             #
#                                                         #
#                                                         #
#                                                         #
#         CYKL ZAPIS WEJSC/WYKONANIE/ODCZYT WYJSC         #
#         def set_NGET(self, ins):                        #
#              self.set_INS(ins)                          #
#              self.next_S()                              #
#             return self.get_OUTP()                      #
#                                                         #
###########################################################

###########################################################

######KLASA RODZIC OBIEKTOW#####
class OBJECT():
    def set_NGET(self, ins):
        self.set_INS(ins)
        self.next_S()
        return self.get_OUTP()

    def set_INS(self, IN):
        self.ins = IN

    def get_OUTP(self):
        return self.out
    
#######SILNIK DC##########
class DC_ENGINE(OBJECT):
    def __init__(self, dt):
        self.ins = 0
        self.out = 0

        self.u = 0
        self.w = 0
        self.i = 0  # [A]
        self.mop = 0
        self.J = 0.11
        self.R = 3
        self.L = 10e-3
        self.kfi = 2.23
        self.dt = dt
        self.i_lim = 20

        self.Ai = -self.R/self.L
        self.Bi = [1/self.L, -self.kfi/self.J]

        self.Aw = self.kfi/self.J
        self.Bw = -1/self.J

    def next_S(self):
        self.u = self.ins
        self.i = self.i + \
            ((self.Bi[1] * self.w) + (self.Ai * self.i) +
             (self.Bi[0] * (self.ins))) * self.dt
        # LIMIT PRADOWY
        if self.i_lim > 0:
            if self.i > self.i_lim:
                self.i = self.i_lim
            elif self.i < -self.i_lim:
                self.i = -self.i_lim
        self.w = self.w + \
            ((self.Bi[0] * (-self.mop)) + (self.Aw * self.i)) * self.dt
        self.out = self.w

##########REGULATOR PID###########
class PID_REG(OBJECT):
    def __init__(self, dt, Kp, Ki):
        self.Kp = Kp
        self.Ki = Ki
        self.Daq = 0
        self.Iaq = 0
        self.Paq = 0
        self.err = 0
        self.err_s = 0
        self.dt = dt
        self.windup = 100

    def next_S(self):
        self.err = self.ins
        self.Iaq = self.Iaq + self.Ki*self.err * self.dt
        # WINDUP
        if self.windup > 0:
            if self.Iaq > self.windup:
                self.Iaq = self.windup
            if self.Iaq < -self.windup:
                self.Iaq = -self.windup
        ######
        self.Paq = self.Kp * self.err
        self.Daq = self.Kp * self.dt*self.err*self.err_s
        self.out = self.Paq + self.Iaq + self.Daq
        self.err_s = self.ins
        
#############PRZEKSZTALTNIK NAPIECIOWY#################
class DC_CONV(OBJECT):
    def __init__(self, dt):
        self.ins = 0
        self.out = 0

        self.uin = 0

        Tprz = 1/(2*3.14*50)
        self.dt = dt
        ###### MODEL DYSKRETNY OBIEKTU INERCYJNEGO I rz.#########
        self.kZ = dt/(Tprz+dt)
        self.aZy = Tprz/(Tprz + dt)
        self.uin = 0
        self.wyj_prz = 0
        self.limu = 400

    def next_S(self):
        self.wyj_prz = self.ins*self.kZ + self.wyj_prz*self.aZy
        if self.limu > 0:
            if self.wyj_prz > self.limu:
                self.wyj_prz = self.limu
            elif self.wyj_prz < -self.limu:
                self.wyj_prz = -self.limu
        self.out = self.wyj_prz
        
#########OPOZNIENIE, DLA 0 BRAK##########
class DELAY(OBJECT):
    def __init__(self, n):
        self.arr = []
        self.ins = None
        for i in range(n+1):
            self.arr.append(0)
        self.out = (lambda x: self.arr[-1])(None)

    def next_S(self):
        self.arr.pop(-1)
        self.arr.insert(0, self.ins)
        
#######SUMATOR +-#########
class DIFFER(OBJECT):
    def __init__(self, wz):
        self.wz = wz
        self.ins = 0
        self.out = 0
        self.error = 0

    def next_S(self):
        self.error = self.wz - self.ins
        self.out = self.error


def try_default(v, default):
    try:
        return float(v)
    except:
        return default


def try_float(v):
    try:
        return float(v)
    except:
        return v
###########GLOWNA FUNKCJA SYMULACJI########


def simulation(c, D_R, D_S, DOP):
    #####POBRANIE DANYCH Z POL####
    R = D_S[0].get()
    L = D_S[1].get()
    kfi = D_S[2].get()
    J = D_S[3].get()
    dt = D_S[4].get()
    nop = D_S[5].get()
    Tsim = D_S[6].get()

    w_zad = D_R[0].get()
    antiw = D_R[1].get()
    limi = D_R[2].get()
    limu = D_R[3].get()

    mop = D_OP[1].get()
    top = D_OP[0].get()

    mop = try_float(mop)
    top = try_float(top)
    # ZAMIANA NA FLOATA LUB BRAK ZMIANY
    R = try_float(R)
    L = try_float(L)
    kfi = try_float(kfi)
    J = try_float(J)
    dt = try_float(dt)

    w_zad = try_float(w_zad)
    antiw = try_float(antiw)
    limi = try_float(limi)
    limu = try_float(limu)

    try:
        nop = int(nop)
    except:
        pass
    #######ZAMIANA NA FLOATA LUB USTAWIENIE WARTOSCI DOMYSLNEJ#####
    Tsim = try_default(Tsim, 1)
    mop = try_default(mop, 4)
    top = try_default(top, 0.5)

    if not isinstance(dt, (float)):
        dt = 0.001

    wzarr = []
    arrw = []
    arri = []
    arru = []
    tt = []
    ###############TWORZENIE OBIEKTOW/SPRAWDZAMY CZY USTAWIONO DANA I PRZYPISUJEMY#########
    silnik = DC_ENGINE(dt)
    if isinstance(R, (int, float)):
        silnik.R = R
    if isinstance(L, (int, float)):
        silnik.L = L
    if isinstance(kfi, (int, float)):
        silnik.kfi = kfi
    if isinstance(J, (int, float)):
        silnik.J = J
    if isinstance(limi, (int, float)):
        silnik.i_lim = limi

    przeksztaltnik = DC_CONV(dt)
    if isinstance(limu, (int, float)):
        przeksztaltnik.limu = abs(limu)

    if isinstance(nop, (int)):
        opoznienie = DELAY(nop)
    else:
        opoznienie = DELAY(0)

    if isinstance(w_zad, (int, float)):
        err = DIFFER(w_zad)
    else:
        if var.get() == 2:
            err = DIFFER(10)
        else:
            err = DIFFER(100)

    try:
        Top = nop*dt
    except:
        Top = 0

    if var2.get() == 2:
        ######METODA M##########
        a0 = silnik.kfi
        a1 = silnik.R*silnik.J
        a2 = silnik.J*silnik.L
        Kp_M = (a1*a1 - 2*a2*a0)/(2*a2*a0)
        Ki_M = (a2*a2 + 2*a0*a0*Kp_M)/(2*a1*a0)
        regulator = PID_REG(dt, Kp_M, Ki_M)
    else:
        # Metoda realizacji reg. IMC za pomoca PI dla obiektu inercyjnego II rzędu.
        Te = silnik.L/silnik.R  # MAŁA STALA CZASOWA
        Tm = silnik.J*silnik.R/silnik.kfi  # DUZA STALA CZASOWA

        Kp_IMC = Tm/(silnik.kfi*(Te+Top))
        Ki_IMC = Tm*Kp_IMC
        regulator = PID_REG(dt, Kp_IMC, Ki_IMC)

    if isinstance(antiw, (int, float)):
        regulator.windup = antiw

    if var.get() == 2:
        wz = [[lambda x:silnik.i]]
        d = [arrw, [arri, wzarr], arru]
        regulator.Ki = regulator.Ki
        regulator.Kp = regulator.Kp
    else:
        wz = [[lambda x:silnik.w]]
        d = [[arrw, wzarr], arri, arru]

    obiekty = [err, regulator, przeksztaltnik, silnik, opoznienie]
    t = 0

    ####PETLA SYMULACJI###################
    for i in range(int(Tsim/dt)):
        t = t+dt
        if t > top:
            silnik.mop = mop
        sygnal = obiekty[0].set_NGET(wz[0][0](None))
        for j in range(1, len(obiekty)):
            sygnal = obiekty[j].set_NGET(sygnal)
        arrw.append(silnik.w)
        arri.append(silnik.i)
        arru.append(silnik.u)
        tt.append(t)
        wzarr.append(err.wz)
    #####################################
    # USUWAMY STARE WYKRESY A NASTEPNIE RYSUJEMY NOWE
    try:
        for x in c:
            x.get_tk_widget().destroy()
    except:
        pass
    for i in range(3):
        fig = plt.Figure(figsize=(5, 4), dpi=100)
        if len(d[i]) == 2:
            ax = fig.add_subplot(111)
            ax.plot(tt, d[i][0], tt, d[i][1])
        else:
            ax = fig.add_subplot(111)
            ax.plot(tt, d[i])
        ax.grid()
        canvas = FigureCanvasTkAgg(fig, master=draw_frame)
        canvas.get_tk_widget().grid(row=2, column=i)
        c.append(canvas)


########INICJACJA OKNA###############
c = []
root = tkinter.Tk()
root.wm_title("STEROWANIE SILNIKIEM DC")
root.geometry("1500x750")
var = tkinter.IntVar()
var2 = tkinter.IntVar()
#####RAMKA NA KTOREJ BEDA WYKRESY######
draw_frame = tkinter.Frame(root, bg="orange", width=1200, height=500)
draw_frame.place(x=0, y=350)
####ELEMENTY I POLA EDYCJI######
D_S = [None, None, None, None, None, None, None]
N_S = ["Opor R = (3)", "Indukcyjnosc L = (10e-3)", "Stala kfi = (2.23)", "Moment bezw. J = (0.11)",
       "czas probk. dt = (0.001)", "ilosc PROBEK opoznienia int n = (0)", "Czas symulacji = (1)"]

tkinter.Label(root, text="SILNIK DC DANE:", foreground="blue",
              pady=10).grid(row=0, column=1)

for i in range(len(D_S)):
    description = tkinter.Label(
        root, text=N_S[i], foreground="blue", pady=10).grid(row=2+i, column=0)
    D_S[i] = tkinter.Entry(root, width=10)
    D_S[i].grid(row=2+i, column=1)


tkinter.Label(root, text="REGULATOR DANE:", foreground="blue",
              pady=10).grid(row=0, column=5)

D_R = [None, None, None, None]
N_R = ["Wartosc sterowana (predkosc)", "Metoda M czy (IMC)", "Wartosc zadana = (100 dla w, 10 dla i)",
       "Antiwindup = (100)", "Prad maksymalny = (20)", "Napiecie maksymalne = (400)"]

for i in range(len(N_R)):
    description = tkinter.Label(
        root, text=N_R[i], foreground="blue", pady=10).grid(row=2+i, column=4)

for i in range(len(D_R)):
    D_R[i] = tkinter.Entry(root, width=10)
    D_R[i].grid(row=4+i, column=5)

tkinter.Label(root, text="MOMENT OPOROWY:", foreground="blue",
              pady=10).grid(row=0, column=15)

D_OP = [None, None]
N_OP = [
    "Czas zalaczenia obciazenia = (0.5)", "Wartosc momentu oporowego = (4)"]

for i in range(len(D_OP)):
    description = tkinter.Label(
        root, text=N_OP[i], foreground="blue", pady=10).grid(row=2+i, column=14)
    D_OP[i] = tkinter.Entry(root, width=9)
    D_OP[i].grid(row=2+i, column=16)

R1 = tkinter.Radiobutton(root, text="(Predkosc)", variable=var, value=1)
R1.grid(row=2, column=5)

R2 = tkinter.Radiobutton(root, text="Prad", variable=var, value=2)
R2.grid(row=2, column=6)

R1 = tkinter.Radiobutton(root, text="(IMC)", variable=var2, value=1)
R1.grid(row=3, column=5)

R2 = tkinter.Radiobutton(root, text="M", variable=var2, value=2)
R2.grid(row=3, column=6)
#####POCZATKOWE PUSTE WYKRESY######
for i in range(3):
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(10, 10)
    ax.grid()
    canvas = FigureCanvasTkAgg(fig, master=draw_frame)  # A tk.DrawingArea.
    canvas.get_tk_widget().grid(row=2, column=i)
    c.append(canvas)

tkinter.Label(root, text="WPISZ SWOJE DANE LUB \n ZOSTAW PUSTE POLE, A DOBIERZE SIĘ WARTOSC DOMYSLNA (W NAWIASIE)",
              foreground="red", pady=10).place(x=800, y=150)
tkinter.Label(root, text="WPISZ 0 ABY WYLACZYC OGRANICZENIA LUB ANTIWINDUP",
              foreground="red", pady=10).place(x=800, y=200)
tkinter.Label(root, text="WYLACZ OGRANICZENIA ABY POPRAWNIE STEROWAC PRADEM \n TYLKO M DZIALA POPRAWNIE DLA PRADU",
              foreground="red", pady=10).place(x=800, y=230)

tkinter.Label(root, text="Predkosc", foreground="blue",
              pady=10, background="white").place(x=220, y=350)
tkinter.Label(root, text="Prad", foreground="blue", pady=10,
              background="white").place(x=740, y=350)
tkinter.Label(root, text="Napiecie", foreground="blue",
              pady=10, background="white").place(x=1230, y=350)

####PRZYCISK MOCY######
draw_button = tkinter.Button(
    root, text="SYMULACJA", pady=15, command=lambda: simulation(c, D_R, D_S, D_OP))
draw_button.place(x=700, y=280)


tkinter.mainloop()