import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=[11.75, 8.25])
ax = fig.add_subplot(1, 1, 1)
plt.axis([0, 750, 0, 18])
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

x = np.arange(0, 750, 1)
e = np.power(2.72, -(x/200))

v_ros=15*(1-e)
v_mal=15*e


linia1 = 0*x + 15

linia2 = 0*x[0:300] + v_ros[300]

plt.plot(x[:300],v_ros[0:300], color='black', linewidth=3)
plt.plot(x[300:750],v_ros[300:750], color='black', linewidth=1, linestyle = 'dashed')
plt.plot(x[300:750],v_mal[50:500], color='black', linewidth=3)
plt.plot(x, linia1, color='black', linewidth=1, linestyle = 'dashed')
plt.plot(x[0:300], linia2, color='black', linewidth=1, linestyle = 'dashed')

plt.axvline(x=300, ymin=0, ymax=11.8/18, color='black', linewidth=1, linestyle = 'dashed')

plt.xticks([])
plt.yticks([])

ax.set_yticks([v_ros[300], 15])
ax.set_yticklabels(['Δ$ϑ_d$', 'Δ$ϑ_u$'], fontsize = 16)

ax.set_xticks([[300]])
ax.set_xticklabels(['$t_d$'], fontsize = 16)

ax.text(2, 17,'Δ$ϑ$',  fontsize = 16)
ax.text(750, 0.5,'t',  fontsize = 16)

ax.text(300, v_ros[320],'A',  fontsize = 18)
plt.scatter([300],[v_ros[300]], color='black', s = 50)

#plt.title('Rys. 2.9. Przebieg przyrostu temperatury w pracy dorywczej S2',  
#          y=-0.1, fontsize = 16)
plt.savefig("wykres2.9.svg", format="svg")
plt.savefig("wykres2.9.png", format="png")