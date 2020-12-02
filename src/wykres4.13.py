import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


fig = plt.figure(figsize=[11.75, 8.25])
ax = fig.add_subplot(1, 1, 1)
plt.axis([0, 1000, -2, 2])
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    
plt.xticks([])
plt.yticks([])

x = np.arange(0, 1000, 1)
y1 = 2* np.sin(x/150)
y2 = np.sin((x-100)/150)

plt.axvline(x=570, ymin=0, ymax=18/18, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=470, ymin=0, ymax=18/18, color='black', linewidth=1, linestyle = 'dashed')
plt.axvline(x=120, ymin=0, ymax=18/18, color='black', linewidth=1, linestyle = 'dashed')

ax.plot(x, y1, linewidth=1, color='black',  linestyle  = '-.')
for i in range(30,120,1):
    y1[i] = 0
    y2[i] = 0

for i in range(470,570,1):
    y1[i] = 0
    y2[i] = 0


ax.annotate("", xy=(0, -0.7), xytext=(120, -0.7), arrowprops=dict(arrowstyle="<->"))
ax.text(510, -.45, '$α$',  fontsize = 18)

ax.annotate("", xy=(470, -0.5), xytext=(570, -0.5), arrowprops=dict(arrowstyle="<->"))
ax.text(50, -.6, '$α$',  fontsize = 18)

ax.plot(x, y1, linewidth=3, color='black')
ax.plot(x, y2, linewidth=3, color='black',  linestyle = 'dashed')

legend_elements = [Line2D([0], [0], color='black', lw = 1.5, label='Przebieg napięcia U', ls = '-'),
                   Line2D([0], [0], color = 'black', lw=1, label='Przebieg prądu i.', ls = '--'),
                   Line2D([0], [0], color = 'black', lw=1, label='Napięcie zasilania.', ls = '-.')
                   ]

ax.legend(handles=legend_elements, loc='upper right',markerscale=0.01, fontsize  = 8)


ax.text(-25, 2,'u',  fontsize = 18)
ax.text(2, 2,'$u_M$',  fontsize = 18)
ax.text(2, 1.8,'i',  fontsize = 18)
ax.text(1000, 0.1,'ωt',  fontsize = 18)

plt.savefig("wykres4.13.svg", format="svg")
plt.savefig("wykres4.13.png", format="png")

#Rys. 4.13. Przebiegi prądu i napięć w jednej fazie układu z rys 4.12.