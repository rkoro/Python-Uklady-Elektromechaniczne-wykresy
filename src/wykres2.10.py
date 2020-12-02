import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=[11.75, 8.25])
ax = fig.add_subplot(1, 1, 1)
plt.axis([0, 1000, 0, 24])
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

plt.xticks([])
plt.yticks([])

x = np.arange(0, 1000, 1)
x1 = np.arange(0, 200, 1)
x2 = np.arange(200, 500, 1)
x3 = np.arange(500, 700, 1)
x4 = np.arange(700, 1000, 1)

ftemp1= 15*(1-np.power(2.72, -(x1/100)))+7
ftemp2= 15*(1-np.power(2.72, -(x/100)))+7
fchlodzenie2 = ftemp1[-1]*np.power(2.72, -((np.arange(0, 300, 1))/286))
f_chlodzenie_tlo = ftemp1[-1]*np.power(2.72, -(np.arange(0, 800, 1)/286))
fchlodzenie2[-1] = 7

ax.plot(np.arange(200, 1000, 1), f_chlodzenie_tlo, linewidth=2, color='black', linestyle = "dashed")
ax.plot(x, ftemp2, color='black', linewidth=2,linestyle = "dashed")
ax.plot(x, x*0+max(ftemp1), color='black', linewidth=1, linestyle = 'dashed')
ax.plot(x, x*0+min(ftemp1), color='black', linewidth=1, linestyle = 'dashed')
ax.plot(x, x*0+22, color='black', linewidth=1, linestyle = 'dashed')

ax.plot(x1, ftemp1, color='black', linewidth=3)
ax.plot(x2, fchlodzenie2, color='black', linewidth=3)
ax.plot(x3, ftemp1, color='black', linewidth=3)
ax.plot(x4, fchlodzenie2, color='black', linewidth=3)

ax.text(950, -1,'t',  fontsize = 18)
ax.text(5, 23,'Δ$ϑ$',  fontsize = 18)

ax.set_yticks([ftemp1[-1], ftemp1[0], 22])
ax.set_yticklabels(['Δ$ϑ_p$', 'Δ$ϑ_o$', 'Δ$ϑ_u$'], fontsize = 18)

plt.axvline(x=200, ymin=0, ymax=18/18, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=500, ymin=0, ymax=18/18, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=700, ymin=0, ymax=18/18, color='black', linewidth=1, linestyle = 'dashed')

plt.scatter([200, 500],[ftemp1[199], fchlodzenie2[299]], color='black', s = 50)
ax.text(200, ftemp2[240],'A',  fontsize = 18)
ax.text(515, fchlodzenie2[280],'B',  fontsize = 18)

ax.annotate("", xy=(0, 4), xytext=(200, 4), arrowprops=dict(arrowstyle="<->"))
ax.text(90, 4.5, '$t_p$',  fontsize = 18)

ax.annotate("", xy=(200, 2), xytext=(500, 2), arrowprops=dict(arrowstyle="<->"))
ax.text(250+90, 2.5, '$t_0$',  fontsize = 18)

#plt.title('Rys. 2.10. Przebieg przyrostu temperatury w pracy przerywanej S3.',  
#          y=-0.1, fontsize = 16)
plt.savefig("wykres2.10.svg", format="svg")
plt.savefig("wykres2.10.png", format="png")