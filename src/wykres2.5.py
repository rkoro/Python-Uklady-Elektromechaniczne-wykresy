import matplotlib.pyplot as plt
import matplotlib
import numpy as np

fig = plt.figure(figsize=[ 11.75, 8.25])
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax1.axis([0, 1000, 0, 12])
ax2.axis([0, 1000, 0, 24])

ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')

ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')

ax1.plot(1, 0, ">k", transform=ax1.get_yaxis_transform(), clip_on=False)
ax1.plot(0, 1, "^k", transform=ax1.get_xaxis_transform(), clip_on=False)

ax2.plot(1, 0, ">k", transform=ax2.get_yaxis_transform(), clip_on=False)
ax2.plot(0, 1, "^k", transform=ax2.get_xaxis_transform(), clip_on=False)

x = np.arange(0, 1000, 1)
x1 = np.arange(0, 200, 1)
x2 = np.arange(200, 500, 1)
x3 = np.arange(500, 700, 1)
x4 = np.arange(700, 1000, 1)

P1 = 0 * x1 + 10
P2 = 0 * x2 + 0.01
P2[0] = P1[-1]
P3 = 0 * x3 + 10
P3[0] = P2[-1]
P4 = 0 * x4 + 0.01
P4[0] = P3[-1]

ax1.plot(x1,P1, color='black', linewidth=3)
ax1.plot(x2,P2, color='black', linewidth=3)
ax1.plot(x3,P3, color='black', linewidth=3)
ax1.plot(x4,P4, color='black', linewidth=3)
ax1.text(5, 11,'$P$',  fontsize = 18)
ax1.text(501, 11,'$a)$',  fontsize = 18)
ax1.text(1000,1,'t',  fontsize = 18)


ftemp1= 15*(1-np.power(2.72, -(x1/100)))+7
ftemp2= 15*(1-np.power(2.72, -(x/100)))+7
fchlodzenie2 = ftemp1[-1]*np.power(2.72, -((np.arange(0, 300, 1))/286))
f_chlodzenie_tlo = ftemp1[-1]*np.power(2.72, -(np.arange(0, 800, 1)/286))
fchlodzenie2[-1] = 7

ax2.plot(np.arange(200, 1000, 1), f_chlodzenie_tlo, linewidth=1, color='black', linestyle = "dashed")
ax2.plot(x, ftemp2, color='black', linewidth=1,linestyle = "dashed")
ax2.plot(x, x*0+max(ftemp1), color='black', linewidth=1, linestyle = 'dashed')
ax2.plot(x, x*0+min(ftemp1), color='black', linewidth=1, linestyle = 'dashed')
ax2.plot(x, x*0+22, color='black', linewidth=1, linestyle = 'dashed')

ax2.plot(x1, ftemp1, color='black', linewidth=3)
ax2.plot(x2, fchlodzenie2, color='black', linewidth=3)
ax2.plot(x3, ftemp1, color='black', linewidth=3)
ax2.plot(x4, fchlodzenie2, color='black', linewidth=3)


ax2.text(501, 24,'$b)$',  fontsize = 18)
ax2.text(1000, 1,'t',  fontsize = 18)
ax2.text(5, 23,'Δ$ϑ$',  fontsize = 18)

plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])

ax1.set_yticks([10])
ax1.set_yticklabels(['$P_p$'], fontsize = 18)
ax1.annotate("", xy=(0, 3), xytext=(200, 3), arrowprops=dict(arrowstyle="<->"))
ax1.text(90, 3.5, '$t_p$',  fontsize = 18)


ax1.annotate("", xy=(200, 2), xytext=(500, 2), arrowprops=dict(arrowstyle="<->"))
ax1.text(250+90, 2.5, '$t_0$',  fontsize = 18)


ax1.annotate("", xy=(500, 3), xytext=(700, 3), arrowprops=dict(arrowstyle="<->"))
ax1.text(500+90, 3.5, '$t_p$',  fontsize = 18)


ax1.annotate("", xy=(700, 2), xytext=(1000, 2), arrowprops=dict(arrowstyle="->"))
ax1.text(750+90, 2.5, '$t_0$',  fontsize = 18)



ax2.set_yticks([ftemp1[-1], ftemp1[0], 22])
ax2.set_yticklabels(['Δ$ϑ_p$', 'Δ$ϑ_o$', 'Δ$ϑ_u$'], fontsize = 18)

i = 200
transFigure = fig.transFigure.inverted()
coord1 = transFigure.transform(ax1.transData.transform([x[i],0]))
coord2 = transFigure.transform(ax2.transData.transform([x[i],0]))

line1 = matplotlib.lines.Line2D((coord1[0],coord2[0]),(coord1[1],coord2[1]),
                               transform=fig.transFigure, color = 'black', linestyle ="dashed", linewidth = 1)
i = 500
coord1 = transFigure.transform(ax1.transData.transform([x[i],0]))
coord2 = transFigure.transform(ax2.transData.transform([x[i],0]))

line2 = matplotlib.lines.Line2D((coord1[0],coord2[0]),(coord1[1],coord2[1]),
                               transform=fig.transFigure, color = 'black', linestyle ="dashed", linewidth = 1)
i = 700
coord1 = transFigure.transform(ax1.transData.transform([x[i],0]))
coord2 = transFigure.transform(ax2.transData.transform([x[i],0]))

line3 = matplotlib.lines.Line2D((coord1[0],coord2[0]),(coord1[1],coord2[1]),
                               transform=fig.transFigure, color = 'black', linestyle ="dashed", linewidth = 1)

coord1 = transFigure.transform(ax1.transData.transform([x[i],0]))
coord2 = transFigure.transform(ax2.transData.transform([x[i],0]))

fig.lines = line1, line2, line3


#plt.title('Rys. 2.5. Przebieg obciążenia (a) i przyrostu temperatury (b) \n w pracy przerywanej S3',  
#          y=-0.3, fontsize = 16)
plt.savefig("wykres2.5.svg", format="svg")
plt.savefig("wykres2.5.png", format="png")