# -*- coding: utf-8 -*-
"""

@author: Radas
"""

import matplotlib.pyplot as plt
import numpy as np

podpis = 'Rys 2.2. Przebieg stygnięcia maszyny'

fig = plt.figure(figsize=[14.75, 8.25])
ax = fig.add_subplot(1, 1, 1)
plt.axis([0, 500, 0, 20])

ftsize = 30

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


x = np.arange(0, 500, 1)
e = np.power(2.72, -(x/100))
v=15*e+2

stycz = -0.14964413*x + 17

 #w ptk 150

stycz2 = -0.03343782*x + 10.35945

linia = 0*x + 2

plt.plot(x,v, color='black', linewidth=3)
plt.plot(x[0:101], stycz[0:101], color='black', linewidth=1, linestyle = 'dashed')

plt.plot(x[150:251], stycz2[150:251], color='black', linewidth=1, linestyle = 'dashed')
plt.plot(x, linia, color='black', linewidth=1, linestyle = 'dashed')


plt.axvline(x=100, ymin=0.35/10, ymax=1/10, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=150, ymin=0.35/10, ymax=2.7/10, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=250, ymin=0.35/10, ymax=1/10, color='black', linewidth=1, linestyle = 'dashed')

plt.xticks([])
plt.yticks([])

ax.annotate("", xy=(150, 0.7), xytext=(251, 0.7), arrowprops=dict(arrowstyle="<->"))
ax.annotate("", xy=(0, 0.7), xytext=(100,0.7), arrowprops=dict(arrowstyle="<->"))

plt.text(45, 0.8, 'Θ',  fontsize = ftsize)
plt.text(195, 0.8, 'Θ',  fontsize = ftsize)

ax.set_yticks([2, 17])
ax.set_yticklabels(['Δ$ϑ_u$', 'Δ$ϑ_o$'], fontsize = ftsize)


plt.text(500, 0.5, 't',  fontsize = ftsize)
plt.text(5, 19.5, 'Δ$ϑ$',  fontsize = ftsize)

#plt.title(podpis,  y=-0.1, fontsize = 12)
plt.savefig("2.2.svg", format="svg", bbox_inches='tight')
plt.savefig("2.2.png", format="png", bbox_inches='tight')