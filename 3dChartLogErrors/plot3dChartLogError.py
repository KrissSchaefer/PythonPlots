import matplotlib.pyplot as plt
from matplotlib import rc
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import numpy as np

#Set globally font type and size
rc('font',size=14)
rc('font',family='serif')
rc('axes',labelsize=14)

#Set markers and colors
markers = ['s', 'o', 'v', '^',
           '*', 'p', '+', 'x',
           'h', '<', '>', 'H',
           'D', 'd']

colors = {'white': (216/255., 202/255., 168/255.) ,
          'lightGreen': (92/255., 131/255., 47/255.),
          'green': (40/255., 73/255., 7/255.),
          'brown': (56/255., 37/255., 19/255.),
          'grey': (54/255., 57/255., 66/255.)}
colorsSorted = [colors['white'], colors['lightGreen'], colors['green'], colors['brown'],  colors['grey']]

#Read data
xs = []
ys = []
zs = []
zsErr = []
with open('data.dat') as inFile:
    for line in inFile:
        line = line.rstrip('\n')
        splitted = line.split()
        
        xs.append(float(splitted[0]))
        ys.append(float(splitted[1]))
        zs.append(float(splitted[2]))
        zsErr.append(float(splitted[3]))

#Create plot
plt.clf()
plt.figure(num=1, figsize=(12, 9), dpi=100, facecolor='w', edgecolor=None)
ax = plt.subplot(111, projection='3d')

#Plot
xs = np.log10(xs)
ax.plot(xs, ys, zs, color=colorsSorted[1], marker=markers[0], ls='', label=r'Data')
for j in range(0, len(zs)):
    ax.plot([xs[j], xs[j]], [ys[j], ys[j]], [zs[j]-zsErr[j], zs[j]+zsErr[j]], color=colorsSorted[1], marker='_')

xMin = np.min(xs)
xMax = np.max(xs)
xLin = np.linspace(xMin, xMax, num=20)
yMin = np.min(ys)
yMax = np.max(ys)
yLin = np.linspace(yMin, yMax, num=20)
grid_x, grid_y = np.meshgrid(xLin, yLin)
grid_z = griddata((xs, ys), zs, (grid_x, grid_y), method='cubic')
ax.plot_wireframe(grid_x, grid_y, grid_z, rstride=1, cstride=1, color=colorsSorted[0], label='Cubic spline')
print('# nans: ',np.isnan(grid_z).sum())

#Set ticks and labels
xticks = np.logspace(3, 7, 5)
ax.set_xticks(np.log10(xticks))
ax.set_xticklabels(['%.e' % (xticks[i]) for i in range(0, len(xticks))], va='center', ha='right')

ylabels = np.arange(-1.1, 0, .2)
ax.set_yticks(ylabels)
ax.set_yticklabels(ylabels, va='center', ha='left')
ax.set_ylim(-1.1, 0)

ax.set_xlabel('\n' + r'$N$', linespacing=2)
ax.set_ylabel('\n' + r'$b_\mathrm{pop}$', linespacing=2)
ax.set_zlabel('\n' + r'$f$', linespacing=2)

ax.set_zlim(.05, 1.3)

#Set title
ax.set_title('A', x=0, y=0.95, loc='left', weight='bold')

#Set key
handles, labels = ax.get_legend_handles_labels()    
lgd = plt.legend(handles, labels, bbox_to_anchor=(1., 1.), loc='upper right', numpoints=1, ncol=1)

#Set grid
ax.w_xaxis.set_pane_color((0, 0, 0, 0))
ax.w_yaxis.set_pane_color((0, 0, 0, 0))
ax.w_zaxis.set_pane_color((0, 0, 0, 0))

#Set intial view
ax.azim = -45
ax.elev = 30

#Save and show figure
figName = '3dChart.pdf'
plt.savefig(figName, bbox_inches='', bbox_extra_artists=(lgd,), facecolor='w', edgecolor=None, dpi=100)
plt.show()
