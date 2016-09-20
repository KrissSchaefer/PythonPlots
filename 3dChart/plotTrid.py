import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

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

#Create data
#Function
def Trid():
    func = lambda x, y: np.power(x-1., 2) + np.power(y-1, 2) - x*y
    return func
function = Trid()

#Data points of function
xs = np.arange(-4, 4, step=1.5)
ys = np.arange(-4, 4, step=1.5)
Xs, Ys = np.meshgrid(xs, ys)

xData = []
yData = []
zData = []
for x, y in zip(Xs, Ys):
    xData.extend(x)
    yData.extend(y)
    zData.extend(function(x, y))

#Create plot
plt.clf()
plt.figure(num=1, figsize=(12, 9), dpi=100, facecolor='w', edgecolor=None)
ax = plt.subplot(111, projection='3d')

#Plot
xPlot = np.arange(-4, 4, step = .5)
yPlot = np.arange(-4, 4, step = .5)
XPlot, YPlot = np.meshgrid(xPlot, yPlot)
ax.plot(xData, yData, zData, color=colorsSorted[1], marker=markers[0], ls='', label='Data')

xMin = np.min(xData)
xMax = np.max(xData)
xLin = np.linspace(xMin, xMax, num=20)
yMin = np.min(yData)
yMax = np.max(yData)
yLin = np.linspace(yMin, yMax, num=20)
grid_x, grid_y = np.meshgrid(xLin, yLin)
grid_z = griddata((xData, yData), zData, (grid_x, grid_y), method='cubic')
ax.plot_wireframe(grid_x, grid_y, grid_z, rstride=1, cstride=1, color=colorsSorted[0], label=r'Cubic spline')
print('# nans: ',np.isnan(grid_z).sum())

#Set labels
ax.set_xlabel('\n' + r'$x$', linespacing=1)
ax.set_ylabel('\n' + r'$y$', linespacing=1)
ax.set_zlabel('\n' + r'$f(x, y)$', linespacing=1)

xlabels = np.arange(-4, 5, 1)
ax.set_xticks(xlabels)
ax.set_xticklabels(xlabels, va='center', ha='left')
ax.set_xlim(-4, 4)

ylabels = np.arange(-4, 5, 1)
ax.set_yticks(ylabels)
ax.set_yticklabels(ylabels, va='center', ha='right')
ax.set_ylim(-4, 4)

ax.set_zlim(-5, 50)

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
ax.azim = 45
ax.elev = 25  

#Save and show figure
figName = 'trid.pdf'
plt.savefig(figName, bbox_inches='tight', bbox_extra_artists=(lgd,), facecolor='w', edgecolor=None, dpi=100)
plt.show()
