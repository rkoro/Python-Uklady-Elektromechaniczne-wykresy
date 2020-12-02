import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=[8.25, 11.75])
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax1.axis([0, 500, 0, 16])
ax2.axis([0, 500, 0, 18])

ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')

ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')


ax1.plot(1, 0, ">k", transform=ax1.get_yaxis_transform(), clip_on=False)
ax1.plot(0, 1, "^k", transform=ax1.get_xaxis_transform(), clip_on=False)


ax2.plot(1, 0, ">k", transform=ax2.get_yaxis_transform(), clip_on=False)
ax2.plot(0, 1, "^k", transform=ax2.get_xaxis_transform(), clip_on=False)

x = np.arange(0, 500, 1)
e = np.power(2.72, -(x/100))

v=15*(1-e)

P = 0*x+13
asymptota = 0*x + 15

ax1.plot(x,P, color='black', linewidth=3)
ax1.text(10, 16,'$P$',  fontsize = 18)
ax1.text(251, 16,'$a)$',  fontsize = 18)
ax1.text(500, 0.2,'t',  fontsize = 18)

ax2.plot(x,v, color='black', linewidth=3)
ax2.text(10, 18,'Δ$ϑ$',  fontsize = 18)
ax2.text(251, 16,'$b)$',  fontsize = 18)
ax2.text(500, 0.1,'t',  fontsize = 18)
#rotation=135

plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])

ax1.set_yticks([13])
ax1.set_yticklabels(['$P_c$'], fontsize = 18)


ax2.set_yticks([15])
ax2.set_yticklabels(['Δ$ϑ_o$'], fontsize = 18)

ax2.plot(x,asymptota, color='black', linewidth=1, linestyle = 'dashed')

#plt.title('Rys. 2.3. Przebieg obciążenia (a) i przyrostu temperatury \n w pracy ciągej S1',  
#          y=-0.2, fontsize = 18)
plt.savefig("wykres2.3.svg", format="svg")
plt.savefig("wykres2.3.png", format="png")