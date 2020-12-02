# -*- coding: utf-8 -*-
"""
@author: Radas
"""

import matplotlib.pyplot as plt
import numpy as np

podpis = 'Rys. 3.6. Porównanie charakterystyk mechanicznych maszyny obcowzbudnej prądu stałego \n przy znamionowym (mniej pochylona linia) i osłabionym wzbudzeniu (bardziej pochylona linia).'

fig = plt.figure(figsize=[ 14.75, 8.25])
ax = fig.add_subplot(1, 1, 1)
plt.axis([-250, 250, 0, 20])

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

#Ustawienie osi ##################################################
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position(('outward', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])

ftsize = 30

plt.text(3, 19  , '$Ω$',  fontsize = ftsize)
plt.text(240, -1.5, '$M$',  fontsize = ftsize)

x = np.arange(-250, 250, 1)
y = - 0.002*x + 6
v = - 0.04*x + 11.5

plt.plot(x,y, color='black', linewidth=3)
plt.plot(x,v, color='black', linewidth=3)

plt.text(12, 11.5, '$Ω_0 =$',  fontsize = ftsize)
plt.text(-50.5, 6.8, '$Ω_{0N} = $',  fontsize = ftsize)


plt.text(60, 10.4, '${\\frac{U}{k_N}}$',  fontsize = 1.4*ftsize)

plt.text(5, 7, '${\\frac{U}{k}}$',  fontsize = 1.4*ftsize)


plt.text(-140, 16.2, '$k < k_N$',  fontsize = ftsize, rotation = -30)
plt.text(-220, 6.7, '$k = k_N$',  fontsize = ftsize)
plt.text(0, -0.8, '0',  fontsize = ftsize)

#plt.title(podpis,  y=-0.12, fontsize = 12)
plt.savefig("3.61.svg", format="svg", bbox_inches='tight')
plt.savefig("3.61.png", format="png", bbox_inches='tight')