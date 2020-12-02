import matplotlib.pyplot as plt
import matplotlib
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
x1 = (np.arange(0, 200, 1))
x2 = np.arange(200, 500, 1)

P1 = 0*x1+13
P2 = 0*x2+0.1
P2[0] = P1[-1]
ftemp1= 15*(1-np.power(2.72, -(x1/100)))
ftemp2= 15*(1-np.power(2.72, -(x2/100)))
fchlodzenie2 = ftemp1[-1]*np.power(2.72, -((np.arange(0, 300, 1))/100))

ax1.plot(x1,P1, color='black', linewidth=3)
ax1.plot(x2,P2, color='black', linewidth=3)
ax1.text(5, 15,'$P$',  fontsize = 18)
ax1.text(251, 16,'$a)$',  fontsize = 18)
ax1.text(500, .5,'t',  fontsize = 18)

ax2.plot(x1, ftemp1, color='black', linewidth=3)
ax2.plot(x2, fchlodzenie2, color='black', linewidth=3)
ax2.plot(x2, ftemp2, color='black', linewidth=2, linestyle = "dashed")

asymptota = 0*x + 15
ax2.plot(x,asymptota, color='black', linewidth=1, linestyle = 'dashed')
linia_pomocnicza = 0*x1 + ftemp1[-1]
ax2.plot(x1,linia_pomocnicza, color='black', linewidth=1, linestyle = 'dashed')


ax2.text(2, 17,'Δ$ϑ$',  fontsize = 18)
ax2.text(251, 16,'$b)$',  fontsize = 18)
ax2.text(500, 0.5,'t',  fontsize = 18)

plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])
i = 199
transFigure = fig.transFigure.inverted()
coord1 = transFigure.transform(ax1.transData.transform([x[i],0]))
coord2 = transFigure.transform(ax2.transData.transform([x[i],0]))

line = matplotlib.lines.Line2D((coord1[0],coord2[0]),(coord1[1],coord2[1]),
                               transform=fig.transFigure, color = 'black', linestyle ="dashed", linewidth = 1)
fig.lines = line,

ax1.set_yticks([13])
ax1.set_yticklabels(['$P_d$'], fontsize = 18)

ax2.set_yticks([ftemp1[-1], 15])
ax2.set_yticklabels(['Δ$ϑ_d$', 'Δ$ϑ_u$'], fontsize = 18)
ax1.annotate("", xy=(0, 3), xytext=(201, 3), arrowprops=dict(arrowstyle="<->"))
ax1.text(90, 3.2, '$t_d$',  fontsize = 18)



#plt.title('Rys. 2.4. Przebieg obciążenia (a) i przyrostu temperatury (b) \n w pracy dorywczej S2',  
#          y=-0.2, fontsize = 18)
plt.savefig("wykres2.4.svg", format="svg")
plt.savefig("wykres2.4.png", format="png")