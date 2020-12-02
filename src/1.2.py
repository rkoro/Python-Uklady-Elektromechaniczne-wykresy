# -*- coding: utf-8 -*-
"""
@author: Radas
"""

import matplotlib.pyplot as plt
import numpy as np

podpis = 'Rys. 1.2. Ilustracja ustalonego punktu pracy napędu na przecięciu \n charakterystyk mechanicznych silnika i maszyny napędzanej'
ftsize = 30
fig = plt.figure(figsize=[8.25,14.75 ])
ax = fig.add_subplot(1, 1, 1)
plt.axis([0, 400, 0, 70])



ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


plt.xticks([])
plt.yticks([])

x_coordinates = [225]
y_coordinates = [46.2]

plt.scatter(x_coordinates, y_coordinates,  color='black')

x = np.arange(1, 400, 1)
xx= np.power(x,2)
xs = np.arange(-57, 400, 1)

Ms = -0.07*x+62
Mw = 0.0008*xx*1+5

plt.text(390, -3.5, '$M$',  fontsize = ftsize)
plt.text(5, 70, '$Ω$',  fontsize = ftsize)
plt.text(-10, -2.5, '0',  fontsize = ftsize)
plt.text(70, 55, 'Char. silnika',  fontsize = ftsize, rotation = -10)
plt.text(35, 9, 'Char. obciążenia',  fontsize = ftsize, rotation = 25)



#ax.annotate('Ustalony punkt pracy',
#            xy=(252, 11.5), xycoords='data',
#            xytext=(30, 50), textcoords='offset points',
#            arrowprops=dict(facecolor='black', shrink=0.001),
#            horizontalalignment='left', verticalalignment='bottom', fontsize = ftsize)

plt.text(x_coordinates[0]+5, y_coordinates[0], '$A_o$',  fontsize = ftsize)
ax.set_yticks(y_coordinates)
ax.set_yticklabels(['$Ω_o$'], fontsize = ftsize)
ax.set_xticks(x_coordinates)
ax.set_xticklabels(['$M_o$'], fontsize = ftsize)

plt.axhline(y=y_coordinates, xmin=0/12, xmax=0.56, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=x_coordinates, ymin=0/9, ymax=0.65, color='black', linewidth=1, linestyle = 'dashed')

plt.plot(Ms, color='black', linewidth=2)
plt.plot(Mw,  color='black',linewidth=2)



#plt.title(podpis,  y=-0.1, fontsize = 12)
plt.savefig("1.22.svg", format="svg", bbox_inches='tight')
plt.savefig("1.22.png", format="png", bbox_inches='tight')