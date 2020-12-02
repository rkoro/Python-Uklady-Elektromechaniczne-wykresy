# -*- coding: utf-8 -*-
"""
@author: Radas
"""


import matplotlib.pyplot as plt
import numpy as np

podpis= 'Rys. 3.7 Charakterystyki dopuszczalnych parametrów maszyny obcowzbudnej prądu stałego w obydwu strefach regulacji'

fig = plt.figure(figsize=[14.75, 8.25])
ax = fig.add_subplot(1, 1, 1)
plt.axis([0, 500, 0, 22])

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# 
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


plt.xticks([])
plt.yticks([])

ftsize = 22

#plt.text(-13, 17, '',  fontsize = 16, rotation = 90)
plt.text(500, -1, 'Ω',  fontsize = ftsize)

ax.annotate("", xy=(0, 20), xytext=(275, 20), arrowprops=dict(arrowstyle="<->"))
ax.annotate("", xy=(275, 20), xytext=(480, 20), arrowprops=dict(arrowstyle="<->"))

plt.axvline(x=275, ymin=0, ymax=1, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=480, ymin=0, ymax=1, color='black', linewidth=1, linestyle = 'dashed')

ax.set_yticks([5, 7, 12, 15,18])
ax.set_yticklabels(['$U_N$', '$k_N$', '$M_N$', '$P_N$', '$I_N$'], fontsize = ftsize)
ax.set_xticks([275])
ax.set_xticklabels(['$Ω_N$'], fontsize = ftsize)

plt.text(30,20.7, 'I strefa regulacji (stałego momentu)',  fontsize = ftsize)
plt.text(300, 20.7, 'II strefa regulacji (stałej mocy)',  fontsize = ftsize)
plt.text(5, 23, 'I, P, M, K, U',  fontsize = ftsize)

xI = np.arange(0, 275, 1)
xII = np.arange(275, 480, 1)

iI = xI*0 + 18
iII = xII*0 + 18
plt.plot(xI,iI, color='black', linewidth=2)
plt.plot(xII,iII, color='black', linewidth=2)
plt.text(140, 18.2, 'I',  fontsize = ftsize)

uI = xI*5/275
uII = 5 + 0*xII
u = 5 + xI*0

plt.plot(xI,uI, color='black', linewidth=2)
plt.plot(xII,uII, color='black', linewidth=2)
plt.plot(xI,u, color='black', linewidth=1, linestyle = 'dashed')
plt.text(140, 3, 'U',  fontsize = ftsize)

pI = xI*15/275
pII = 15 + 0*xII
p = 15 + xI*0

plt.plot(xI,pI, color='black', linewidth=2)
plt.plot(xII,pII, color='black', linewidth=2)
plt.plot(xI,p, color='black', linewidth=1, linestyle = 'dashed')
plt.text(140, 8.5, 'P',  fontsize = ftsize)

mI = 0*xI  + 12
mII = 12*275/xII
plt.plot(xI,mI, color='black', linewidth=2)
plt.plot(xII,mII, color='black', linewidth=2)
plt.text(40, 12.5, 'M',  fontsize = ftsize)
plt.text(320, 10.5, '$M = M_N$',  fontsize = ftsize)

kI = 0*xI  + 7
kII = 7*275/xII
plt.plot(xI,kI, color='black', linewidth=2)
plt.plot(xII,kII, color='black', linewidth=2)
plt.text(40, 7.5, 'k',  fontsize = ftsize)
plt.text(320, 6.5, '$k = k_N$',  fontsize = ftsize)
plt.text(485, 0.5, '$Ω_{max}$',  fontsize = ftsize)
plt.text(-10, 0, '$0$',  fontsize = ftsize)

plt.text(368, 10.4, '$\\frac{Ω_{N}}{Ω}}$',  fontsize = 1.4*ftsize)
plt.text(363, 6.25, '${\\frac{Ω_{N}}{Ω}}$',  fontsize = 1.4*ftsize)

#plt.title(podpis,  y=-0.1, fontsize = 12)
plt.savefig("3.71.svg", format="svg", bbox_inches='tight')
plt.savefig("3.71.png", format="png", bbox_inches='tight')