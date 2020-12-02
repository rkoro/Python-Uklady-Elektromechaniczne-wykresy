
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=[11.75, 8.25])
ax = fig.add_subplot(1, 1, 1)
plt.axis([0, 500, 0, 20])

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


plt.xticks([])
plt.yticks([])


plt.text(-13, 17, '',  fontsize = 16, rotation = 90)
plt.text(500, -1, '$f_s$',  fontsize = 16)


plt.axvline(x=275, ymin=0, ymax=1, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=480, ymin=0, ymax=1, color='black', linewidth=1, linestyle = 'dashed')

ax.set_yticks([12, 7, 8.5, 18,10, 1])
ax.set_yticklabels(['$U_{sn}$', '$K_n$', '$M_n$', '$P_n$', '$I_n$', '$U_s$'], fontsize = 16)
ax.set_xticks([275, 480])
ax.set_xticklabels(['$f_{sn}$'], fontsize = 16)

plt.text(50, -0.7, 'I strefa regulacji (stałego momentu)',  fontsize = 14)
plt.text(285, -0.7, 'II strefa regulacji (stałej mocy)',  fontsize = 14)
plt.text(5, 20, '$U_s  , P , M , M_{k} , I$, Ψ',  fontsize = 16)
plt.text(-10, -1, '0',  fontsize = 16)


xI = np.arange(0, 275, 1)
xII = np.arange(275, 480, 1)


#Prad
iI = xI*0 + 10
iII = xII*0 + 10
plt.plot(xI,iI, color='black', linewidth=2)
plt.plot(xII,iII, color='black', linewidth=2)



#napiecie

    
uI = xI*12/275
uII = 12 + 0*xII
u = 12 + xI*0

for i in range(30):
    uI[i] = 1


    
uI[26] = 1.03
uI[27] = 1.10
uI[28] = 1.12
uI[29] = 1.17
uI[30] = 1.2




plt.plot(xI,uI, color='black', linewidth=2)
plt.plot(xII,uII, color='black', linewidth=2)
plt.plot(xI,u, color='black', linewidth=1, linestyle = 'dashed')
plt.text(150, 5.5, '$U_{sn}(f_s/f_{sn})$',  fontsize = 16, rotation = 40)

#moc
pI = xI*18/275
pII = 18 + 0*xII
p = 18 + xI*0
plt.plot(xI,pI, color='black', linewidth=2)
plt.plot(xII,pII, color='black', linewidth=2)
plt.plot(xI,p, color='black', linewidth=1, linestyle = 'dashed')
plt.text(170, 12.5, '$P_n(f_s/f_{sn})$',  fontsize = 16, rotation = 50)

#
mI = 0*xI  + 16
mII = 16* np.power(275/xII, 2)
plt.plot(xI,mI, color='black', linewidth=2)
plt.plot(xII,mII, color='black', linewidth=2)
plt.text(40, 16.5, '$M_{kn}$',  fontsize = 16)
plt.text(400, 7, '$M_n(f_s/f_{sn})$',  fontsize = 16, rotation = -15)


mIc = 0*xI  + 8.5
mIIc = 8.5*275/xII
plt.plot(xI,mIc, color='black', linewidth=2)
plt.plot(xII,mIIc, color='black', linewidth=2)
plt.text(40, 8.75, '$M_n$',  fontsize = 16)
plt.text(300, 5.5, '$M_n(f_s/f_{sn})$',  fontsize = 16, rotation = -20)

yI = 0*xI  + 5
yII = 5*275/xII
plt.plot(xI,yI, color='black', linewidth=2)
plt.plot(xII,yII, color='black', linewidth=2)
plt.text(40, 5.5, 'ψ',  fontsize = 16)
plt.text(300, 3, '$Ψ_n(f_s/f_{sn})$',  fontsize = 16, rotation = -15)


plt.savefig("wykres4.17.svg", format="svg")
plt.savefig("wykres4.17.png", format="png")
#Rys. 4.17. Sterowanie częstotliwosciowe silnika indukcyjnego = charakterystyki częstotliwoci: napięcia stojana (Us), strumienia silnika Ψ, momentu krytycznego (Mk) oraz granicznych wartosci pracy ciągłej: prądu(I), momentu (M) i mocy (P). 