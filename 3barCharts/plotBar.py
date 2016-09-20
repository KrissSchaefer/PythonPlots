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

#Create plot
plt.clf()
plt.figure(num=1, figsize=(12, 9), dpi=100, facecolor='w', edgecolor=None)
fig, axes = plt.subplots(nrows=1, ncols=3, sharex=False, sharey=True)

text = ['Up', 'Flat', 'Down']
for i in range(0, 3):
    filename = 'data' + str(i+1) + '.dat'

    #Read in data
    types = []
    As = []
    Bs = []
    with open(filename) as inFile:
        for line in inFile:
            if not line.startswith('#'):
                line = line.rstrip('\n')
                splitted = line.split()
                types.append(splitted[0])
                As.append(float(splitted[1]))
                Bs.append(float(splitted[2]))

    #Plot data
    width = 0.3
    axes[i].bar([i + 1*width for i in range(len(types))], As,
             width=width, color=colors['white'], edgecolor='none', align='center', hatch='',
             log=False, label=r'A')
    axes[i].bar([i + 2*width for i in range(len(types))], Bs,
             width=width, color=colors['lightGreen'], edgecolor='none', align='center', hatch='',
             log=False, label=r'B')

    #Set xticks and xticklabels
    axes[i].set_xticks([i + 1.5*width for i in range(len(types))])
    axes[i].set_xticklabels(['{}'.format(N) for N in types])

    #Set vertical grid lines
    axes[i].yaxis.grid(True)

    #Set title
    plt.text(0.1, 0.95, text[i], transform=axes[i].transAxes, color=colors['green'])

#Set axis labels
axes[0].set_ylabel(r'Percentage')
axes[1].set_xlabel(r'Type')        

#Set key
handles, labels = axes[0].get_legend_handles_labels()
lgd = plt.legend(handles, labels, bbox_to_anchor=(1., 1.), loc='upper right', numpoints=1, ncol=1)

plt.subplots_adjust(wspace=0, hspace=0)

#Save and show figure
figName = '3barCharts.pdf'
plt.savefig(figName, bbox_inches='tight', bbox_extra_artists=(lgd,), facecolor='w', edgecolor=None, dpi=100)
plt.show()



