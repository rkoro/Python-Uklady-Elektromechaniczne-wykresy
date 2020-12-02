    # -*- coding: utf-8 -*-
"""

@author: Radas
"""


import matplotlib.pyplot as plt
import numpy as np

podpis = 'Rys 2.1. Przebieg nagrzewania maszyny'
ftsize = 30

fig = plt.figure(figsize=[14.75, 8.25])
ax = fig.add_subplot(1, 1, 1)
plt.axis([0, 500, 0, 20])
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

x = np.arange(0, 500, 1)
e = np.power(2.72, -(x/100))
v=15*(1-e) +2

# styczna w ptk 0 #############################################
b = 2
a = 2.15039584 - b
stycz = a*x + b
# styczna w ptk 150 ########################################


linia = 0*x + 17

y = 0.03343782*x + 8.640546

plt.plot(x,v, color='black', linewidth=3)
plt.plot(x[0:100], stycz[0:100], color='black', linewidth=1, linestyle = 'dashed')
plt.plot(x[150:250], y[150:250], color='black', linewidth=1, linestyle = 'dashed')
plt.plot(x, linia, color='black', linewidth=1, linestyle = 'dashed')

plt.axvline(x=100, ymin=17/20, ymax=18/20, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=150, ymin=68/100, ymax=18/20, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=250, ymin=90/100, ymax=17/20, color='black', linewidth=1, linestyle = 'dashed')

plt.xticks([])
plt.yticks([])

ax.annotate("", xy=(0, 17.5), xytext=(100, 17.5), arrowprops=dict(arrowstyle="<->"))
ax.annotate("", xy=(150, 17.5), xytext=(251, 17.5), arrowprops=dict(arrowstyle="<->"))

plt.text(45, 17.7, 'Θ',  fontsize = ftsize)
plt.text(195, 17.7, 'Θ',  fontsize = ftsize)

plt.text(500, 0.5, 't',  fontsize = ftsize)
plt.text(5, 19.5, 'Δ$ϑ$',  fontsize = ftsize)

ax.set_yticks([2, 17])
ax.set_yticklabels(['Δ$ϑ_o$', 'Δ$ϑ_u$'], fontsize = ftsize)

#plt.title(podpis,  y=-0.1, fontsize = 12)
plt.savefig("2.12.svg", format="svg", bbox_inches='tight')
plt.savefig("2.12.png", format="png", bbox_inches='tight')