import matplotlib.pyplot as plt
from matplotlib import rc

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

#readin data
fsTrue = []
fs = []
fsErr = []
with open('data.dat') as inFile:
    for line in inFile:
        line = line.rstrip('\n')
        splitted = line.split()
        fTrue = float(splitted[0])
        f = float(splitted[1])
        fErr = float(splitted[2])

        fsTrue.append(fTrue)
        fs.append(f)
        fsErr.append(fErr)

#Create plot
plt.clf()
plt.figure(num=1, figsize=(12, 9), dpi=100, facecolor='w', edgecolor=None)
ax = plt.subplot(111)

#Plot data
x = range(1, len(fsTrue)+1)
ax.plot(x, fsTrue,
        color=colorsSorted[0], marker=None, ls='-', lw=3, label=r'Exact')
ax.errorbar(x, fs, yerr=fsErr,
            color=colorsSorted[1], marker=markers[1], ls='', label=r'Guess')

#Set axis labels
ax.set_xlabel(r'Rank')
ax.set_ylabel(r'$f$')
ax.set_xlim(-2, 102)
#ax.set_yscale('log', nonposy='clip')

#Set grid lines
ax.grid(True)

#Set key
handles, labels = ax.get_legend_handles_labels()
lgd = plt.legend(handles, labels, bbox_to_anchor=(1., 1.), loc='upper right', numpoints=1, ncol=1)

#Set title
ax.set_title(' A', x=0, y=1, loc='left', weight='bold')

#Save and show figure
figName = 'f.pdf'
plt.savefig(figName, bbox_inches='tight', bbox_extra_artists=(lgd,), facecolor='w', edgecolor=None, dpi=100)
plt.show()



