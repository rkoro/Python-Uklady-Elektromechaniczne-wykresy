# -*- coding: utf-8 -*-
"""
@author: Radas
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

podpis = "Rys. 4.18. Charakterystyki mechaniczne maszyny indukcyjnej sterowanej częstotliwościowo \n w strefie stałego momentu ($|f|\leq f_N$) i stałej mocy ($|f|\geq f_N$) dla obu kierunków wirowania \n wraz z charakterystykami mechanicznymi obciążenia (zwjiarki - krzywe AB) i punktami pracy"

def wzor_klossa(Mk, skn, fn, fx, wsn, w_array):
    skx = skn * fn/fx
    sx = (wsn*fx/fn - w_array)/(wsn*fx/fn) 
    M = 2*Mk/(((wsn*fx/fn - w_array)/(wsn*fx/fn))/skx + skx/((wsn*fx/fn - w_array)/(wsn*fx/fn)))
    return [M, sx]

def pocz(M_array, Mn, w_array):
    return M_array/M_array[0] * Mn + (M_array - M_array/M_array[0] * Mn) * w_array/w_array.size
    
def pocz_Neg(M_array, Mn, w_array):
    return (M_array/M_array[w_array.size-1] * -Mn) + (M_array - (M_array/M_array[w_array.size-1] * -Mn)) * (((w_array.size-w_array)/w_array.size)-1)
    
def rysuj(M, Mk, w):
    max = np.where(M==Mk)[0][0]
    min = np.where(M==-Mk)[0][0]
    if min > wsn:
        for i in range(wsn, end):
            if M[i] <= -wsn/i*wsn/i*Mk:
                min = i
                break
        
    #Mpocz = pocz(M[0:max], Mn*1.1, w[0:max])
    plt.plot(w[0:max], M[0:max], color='black', linewidth=0.3, linestyle = 'dashed')
    plt.plot(w[max:min], M[max:min], color='black', linewidth=2)
    plt.plot(w[min:end], M[min:end], color='black', linewidth=0.3, linestyle = 'dashed')

def rysuj_Neg(M, Mk, w):
    min = np.where(M==-Mk)[0][0]
    max = np.where(M==Mk)[0][0]
   
    if max < wsn+200 :
        for i in range(wsn, end):
            if M[i] <= wsn/i*wsn/i*Mk:   
                max = i+350
                break
    
    #Mpocz = pocz_Neg(M[min:end], Mn*1.1,w[min:end])
    plt.plot(w[0:max], M[0:max], color='black', linewidth=0.3, linestyle = 'dashed')
    plt.plot(w[max:min], M[max:min], color='black', linewidth=2)
    plt.plot(w[min:end], M[min:end], color='black', linewidth=0.3, linestyle = 'dashed')

def rysuj_strefa2(M, Mk, w, min):
    max = np.where(M==Mk)[0][0]+200
    plt.plot(w[0:max],M[0:max], color='black', linewidth=0.3, linestyle = 'dashed')
    plt.plot(w[max:min], M[max:min], color='black', linewidth=2)
    plt.plot(w[min:end], M[min:end], color='black', linewidth=0.3, linestyle = 'dashed')
    
def rysuj_Neg2(M, Mk, w, max, min):

    plt.plot(w[0:max], M[0:max], color='black', linewidth=0.3, linestyle = 'dashed')
    plt.plot(w[max:min], M[max:min], color='black', linewidth=2)
    plt.plot(w[min:end], M[min:end], color='black', linewidth=0.3, linestyle = 'dashed')
    
def adnotacja(text, x,y,xt,yt):
    ax.annotate(text,
    xy=(x, y), xycoords='data',
    xytext=(xt, yt), textcoords='offset points',
    arrowprops=dict(facecolor='black',  arrowstyle='-'),
    horizontalalignment='left', verticalalignment='bottom', fontsize = ftsize)

    
plt.figure(figsize=[23.5, 16.5])
fig = plt.figure(figsize=[11.75, 8.25])
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.xticks([])
plt.yticks([])



end = 30000
Mn = 8
Mk = 20
sk = 0.15
fn = 800
fx = 800
wsn = 14240

w4 = 30000- 4368
w3 = 30000- 8640
w2 = 30000- 20210
w1 = 30000- 24500

ftsize=12
wys= 0.45


wend1 = np.arange(-end, -wsn, 1)
wend2 = np.arange(wsn, end, 1)

temp1 = np.power(wsn/wend1,2)
temp2 = np.power(wsn/wend2,2)

wst = np.arange(-wsn, wsn, 1)


#Linie stref pracy ################################################################

f1 = 0*wst + Mk
f2 = 0*wst + Mn
f3 = Mk * temp1
f4 = Mk * temp2
f5 = Mn * wsn/wend1
f6 = Mn * wsn/wend2
lwd = 1.3

plt.plot(wst,f1, color='black', linewidth=lwd, linestyle = 'dashed')
plt.plot(wst,f2, color='black', linewidth=lwd, linestyle = 'dashed')
plt.plot(wst,-f1, color='black', linewidth=lwd, linestyle = 'dashed')
plt.plot(wst,-f2, color='black', linewidth=lwd, linestyle = 'dashed')
plt.plot(wend1,f3, color='black', linewidth=lwd, linestyle = 'dashed')
plt.plot(wend1,-f3, color='black', linewidth=lwd, linestyle = 'dashed')
plt.plot(wend2,-f4, color='black', linewidth=lwd, linestyle = 'dashed')
plt.plot(wend2,f4, color='black', linewidth=lwd, linestyle = 'dashed')
plt.plot(wend1,f5, color='black', linewidth=lwd, linestyle = 'dashed')
plt.plot(wend1,-f5, color='black', linewidth=lwd, linestyle = 'dashed')
plt.plot(wend2,-f6, color='black', linewidth=lwd, linestyle = 'dashed')
l1=plt.plot(wend2,f6, color='black', linewidth=lwd, linestyle = 'dashed')

plt.axvline(x=wsn, ymin=95/100, ymax=1/22, color='black', linewidth=lwd, linestyle = 'dashed')
plt.axvline(x=-wsn, ymin=95/100, ymax=1/22, color='black', linewidth=lwd, linestyle = 'dashed')
plt.axvline(x=end, ymin=0.395, ymax=0.605, color='black', linewidth=lwd, linestyle = 'dashed')
plt.axvline(x=-end, ymin=0.395, ymax=0.605, color='black', linewidth=lwd, linestyle = 'dashed')

# Krzywe Klossa #####################################################################
w = np.arange(0, end, 1)
wmin = np.arange(-end, 0, 1)

M10 , s1 = wzor_klossa(Mk, sk, fn, 1.8*fx, wsn, w)
tempos = np.where(M10==Mk)[0][0]
My10= 0.97*Mk*wsn/tempos*wsn/tempos
M10 , s1 = wzor_klossa(My10, sk, fn, 1.8*fx, wsn, w)

M11 , s1 = wzor_klossa(Mk, sk, fn, 1.5*fx, wsn, w)
tempos = np.where(M11==Mk)[0][0]
My11= 0.96*Mk*wsn/tempos*wsn/tempos
M11 , s1 = wzor_klossa(My11, sk, fn, 1.5*fx, wsn, w)


M12 , s1 = wzor_klossa(Mk, sk, fn, -1.5*fx, wsn, wmin)
tempos = np.where(M12==Mk)[0][0]
My12= 2.25*wsn/tempos*wsn/tempos
M12 , s1 = wzor_klossa(My12, sk, fn, -1.5*fx, wsn, wmin)


M13 , s1 = wzor_klossa(Mk, sk, fn, -1.8*fx, wsn, wmin)
tempos = np.where(M13==Mk)[0][0]
My13= 0.18*wsn/tempos*wsn/tempos
M13 , s1 = wzor_klossa(My13, sk, fn, -1.8*fx, wsn, wmin)

M1 , s1 = wzor_klossa(Mk, sk, fn, 800, wsn, w)
M2 , s2 = wzor_klossa(Mk, sk, fn, 550, wsn, w)
M3 , s3 = wzor_klossa(Mk, sk, fn, 300, wsn, w)

M4 , s4 = wzor_klossa(Mk, sk, fn, -300, wsn, wmin)
M6 , s6 = wzor_klossa(Mk, sk, fn, -550, wsn, wmin)
M5 , s5 = wzor_klossa(Mk, sk, fn, -800, wsn, wmin)

x = np.arange(2700, 27000, 1)
e = np.power(2.72, -(x/6000))
v=15*e +2.5

plt.plot(x,v, color='black', linewidth=3)
plt.plot(-x,v, color='black', linewidth=3)

xwpr = [3316+1500, -3316-2500, 3316+6150, -3316-6800, 3316+10700, -3316-11150 , 3316+17730, -3316-18350 , 3316+21880, -3316-22750]
ymx = [0.7,0.7,0.62,0.62,0.58,0.58,0.57,0.57,0.56,0.56]        

for i in range(len(xwpr)):
    plt.axvline(x=xwpr[i], ymin=0.49, ymax=ymx[i], color='black', linewidth=0.5, linestyle = 'dashed')

plt.scatter([x[0], -x[0], x[-1], -x[-1], 3316+1500, -3316-2500, 3316+6150, -3316-6800, 3316+10700, -3316-11150 , 3316+17730, -3316-18350 , 3316+21880, -3316-22750], 
            [v[0], v[0], v[-1], v[-1],Mn+1.2, Mn+0.2,0.7*Mn, 0.67*Mn,0.49*Mn, 0.48*Mn, 0.37*Mn, 0.365*Mn, 0.34*Mn, 0.34*Mn], 
            color='black', s = ftsize+4)

rysuj_strefa2(M1, Mk, w, 16500)
rysuj(M2, Mk, w)
rysuj(M3, Mk, w)
rysuj_strefa2(M10, My10, w, 27640)
rysuj_strefa2(M11, My11, w, 23450)

rysuj_Neg(M4, Mk, wmin)
rysuj_Neg(M5, Mk, wmin)
rysuj_Neg(M6, Mk, wmin)
rysuj_Neg2(M12, My12, wmin,7670,10600)
rysuj_Neg2(M13, My13, wmin, 3350,6000)


## Omegi na osi X.##########################################################################

plt.text(-end -2000, wys,'$-Ω_{max}$',  fontsize = ftsize)
plt.text(-w4, wys,'$-Ω_{s4}$',  fontsize = ftsize)
plt.text(-w3, wys, '$-Ω_{s3}$',  fontsize = ftsize)
plt.text(-wsn, wys,'$-Ω_{sn}$',  fontsize = ftsize)
plt.text(-w2, wys, '$-Ω_{s2}$',  fontsize = ftsize)
plt.text(-w1,wys,'$-Ω_{s1}$',  fontsize = ftsize)

plt.text(end, wys,'$Ω_{max}$',  fontsize = ftsize)
plt.text(w4+25, wys,'$Ω_{s4}$',  fontsize = ftsize)
plt.text(w3+25, wys, '$Ω_{s3}$',  fontsize = ftsize)
plt.text(wsn+25, wys,'$Ω_{sN}$',  fontsize = ftsize)
plt.text(w2+25, wys, '$Ω_{s2}$',  fontsize = ftsize)
plt.text(w1+25,wys,'$Ω_{s1}$',  fontsize = ftsize)


przesuniecie = 2700

plt.text(-w4-przesuniecie, -3*wys,'$-Ω_{4}$',  fontsize = ftsize)
plt.text(-w3-przesuniecie, -3*wys, '$-Ω_{3}$',  fontsize = ftsize)
plt.text(-wsn-przesuniecie, -3*wys,'$-Ω_{N}$',  fontsize = ftsize)
plt.text(-w2-przesuniecie, -3*wys, '$-Ω_{2}$',  fontsize = ftsize)
plt.text(-w1-przesuniecie,-3*wys,'$-Ω_{1}$',  fontsize = ftsize)

przesuniecie = 1900

plt.text(w4 -przesuniecie, -3*wys,'$Ω_{4}$',  fontsize = ftsize)
plt.text(w3 -przesuniecie, -3*wys, '$Ω_{3}$',  fontsize = ftsize)
plt.text(wsn -przesuniecie, -3*wys,'$Ω_{N}$',  fontsize = ftsize)
plt.text(w2 -przesuniecie, -3*wys, '$Ω_{2}$',  fontsize = ftsize)
plt.text(w1 -przesuniecie,-3*wys,'$Ω_{1}$',  fontsize = ftsize)



przesuniecie = 1700
# Zero w punkcie (0,0) oraz os Y ########################################################################

plt.text(-przesuniecie+700, 0.2, '0',  fontsize = ftsize)
plt.text(-przesuniecie, Mk+0.3, '$M_k$',  fontsize = ftsize)
plt.text(-przesuniecie, Mn+0.3, '$M_N$',  fontsize = ftsize)
plt.text(-przesuniecie-300, -Mn-1, '-$M_N$',  fontsize = ftsize)
plt.text(-przesuniecie-300, -Mk-1, '-$M_k$',  fontsize = ftsize)

plt.text(300, 22, 'M',  fontsize = ftsize)
plt.text(32000,-1.8,'$Ω$',  fontsize = ftsize)

plt.text(x[0]-300, v[0]+0.5, 'A',  fontsize = ftsize)
plt.text(x[-1]+500,v[-1],'B',  fontsize = ftsize)

plt.text(-x[0]+300, v[0]+0.5, '$A\'$',  fontsize = ftsize)
plt.text(-x[-1]-1000,v[-1],'$B\'$',  fontsize = ftsize)

# Annotacje ####################################################################################
adnotacja('$M_{kN}$', 16600, 15, 2, 20)
adnotacja('$M_{kN}$', 27000, 4.3, 0, 50)

plt.text(19000, 17.2, '$({\\frac{Ω_{sN}}{Ω})}^2$',  fontsize = 1.4*ftsize)
plt.text(29200, 9.1, '$({\\frac{Ω_{sN}}{Ω})}$',  fontsize = 1.4*ftsize)


adnotacja('$f_1$', 3500, Mk, 2, 20)
adnotacja('$f_2$', 7700, Mk, 2, 20)
adnotacja('$f_N$', 12000, Mk, 2, 20)
adnotacja('$f_3$', 19800, 1.25* Mn, 2, 20)
adnotacja('$f_4$', 24200, 0.85*Mn, 2, 20)

adnotacja('$-f_1$', -3300, -0.98*Mk, 2, 20)
adnotacja('$-f_2$', -7700, -0.98*Mk, 2, 20)
adnotacja('$-f_N$', -12000, -0.98*Mk, 2, 20)
adnotacja('$-f_3$', -20000, -1.3*Mn, -40, -30)
adnotacja('$-f_4$', -24200, -0.9*Mn, -40, -30)

# Legenda #######################################################################################



#plt.title(podpis,  y=-0.1, fontsize = 12)
plt.savefig("4.182.svg", format="svg", bbox_inches='tight')
plt.savefig("4.182.png", format="png", bbox_inches='tight')
