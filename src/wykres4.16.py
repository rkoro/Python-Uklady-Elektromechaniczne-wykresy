import matplotlib.pyplot as plt

import numpy as np

fig = plt.figure(figsize=[11.75, 8.25])
ax = fig.add_subplot(1, 1, 1)
plt.axis([0, 1.1, 0, 18])
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


pkt_x = [16, 4, 1.78, 1]
pkt_y = [0 ,1/4, 1/2, 3/4 ,1]


linia16 = 0*np.arange(0, 0.25, 0.01) +pkt_x[0]
linia4 = 0*np.arange(0, 0.5, 0.01) +pkt_x[1]
linia78 = 0*np.arange(0, 0.75, 0.01) +pkt_x[2]
linia1 = 0*np.arange(0, 1, 0.01) +pkt_x[3]

x = np.arange(0, 1.01, 0.01)
y = 0.001198228 + (271263.9 - 0.001198228)/(1 + np.power(x/0.001920867,2.000186))


ax.set_yticks(pkt_x)
ax.set_yticklabels(pkt_x, fontsize = 16)

ax.set_xticks(pkt_y)
ax.set_xticklabels(pkt_y, fontsize = 16)

plt.plot(x,y, color='black', linewidth=2)

plt.plot(np.arange(0, 0.25, 0.01),linia16, color='black', linewidth=1, linestyle= 'dashed')
plt.plot(np.arange(0, 0.5, 0.01),linia4, color='black', linewidth=1, linestyle= 'dashed')
plt.plot(np.arange(0, 0.75, 0.01),linia78, color='black', linewidth=1, linestyle= 'dashed')
plt.plot(np.arange(0, 1, 0.01),linia1, color='black', linewidth=1, linestyle= 'dashed')

plt.plot(x,y, color='black', linewidth=3)


plt.axvline(x=0.25, ymin=0/100, ymax=16/18, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=0.5, ymin=0/100, ymax=4/18, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=0.75, ymin=0/100, ymax=1.78/18, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=1, ymin=0/100, ymax=1/18, color='black', linewidth=1, linestyle = 'dashed')

plt.text(0.02, 17,'${\\frac{ΔP}{ΔP_{min}}}$',  fontsize = 24)

plt.text(1.05, 0.3,'w',  fontsize = 18)

#plt.title('Rys. 4.16. Wpływ wypadkowego współczynnika mocy na straty rezystancyjne w silniku sterowanym napięciowo.',  
#          y=-0.1, fontsize = 16)
plt.savefig("wykres4.16.svg", format="svg")
plt.savefig("wykres4.16.png", format="png")