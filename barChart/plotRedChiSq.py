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

#Read in data and modify redChiSq to 1./redChiSq
Ns = []
redChiSqs_df = []
redChiSqsErr_df = []
redChiSqs_dfeta = []
redChiSqsErr_dfeta = []
redChiSqs_dfb = []
redChiSqsErr_dfb = []
with open('data.dat') as inFile:
    for line in inFile:
        if not line.startswith('#'):
            line = line.rstrip('\n')
            splitted = line.split()
            N = float(splitted[0])
            redChiSq_df = 1./float(splitted[1])
            redChiSqErr_df = float(splitted[2])*redChiSq_df*redChiSq_df
            redChiSq_dfeta = 1./float(splitted[3])
            redChiSqErr_dfeta = float(splitted[4])*redChiSq_dfeta*redChiSq_dfeta
            redChiSq_dfb = 1./float(splitted[5])
            redChiSqErr_dfb = float(splitted[6])*redChiSq_dfb*redChiSq_dfb
            
            Ns.append(N)
            redChiSqs_df.append(redChiSq_df)
            redChiSqsErr_df.append(redChiSqErr_df)
            redChiSqs_dfeta.append(redChiSq_dfeta)
            redChiSqsErr_dfeta.append(redChiSqErr_dfeta)
            redChiSqs_dfb.append(redChiSq_dfb)
            redChiSqsErr_dfb.append(redChiSqErr_dfb)

#Create plot
plt.clf()
plt.figure(num=1, figsize=(12, 9), dpi=100, facecolor='w', edgecolor=None)
ax = plt.subplot(111)

#Plot data
width = 0.2
ax.bar([i + 1*width for i in range(len(Ns))], redChiSqs_df, yerr=redChiSqsErr_df,
       width=width, color=colorsSorted[0], edgecolor='none', ecolor=colors['grey'], align='center', hatch='',
       log=False, label=r'$\widebar{\delta f}$')
ax.bar([i + 2*width for i in range(len(Ns))], redChiSqs_dfeta, yerr=redChiSqsErr_dfeta,
       width=width, color=colorsSorted[1], edgecolor='none', ecolor=colors['grey'], align='center', hatch='/', 
       log=False, label=r'$\widebar{\delta f}_\eta$')
ax.bar([i + 3*width for i in range(len(Ns))], redChiSqs_dfb, yerr=redChiSqsErr_dfb,
       width=width, color=colorsSorted[2], edgecolor='none', ecolor=colors['grey'], align='center', hatch='//',
       log=False, label=r'$\Delta f_\mathrm{B}$')

#Set xticks and xticklabels
ax.set_xticks([i + 2*width for i in range(len(Ns))])
ax.set_xticklabels(['%.2g' % (N) for N in Ns])

#Set axis labels
ax.set_xlabel(r'$N$')
ax.set_ylabel(r'$(\chi^2/\nu)^{-1}$')

#Set vertical grid lines
ax.yaxis.grid(True)

#Set key
handles, labels = ax.get_legend_handles_labels()
lgd = plt.legend(handles, labels, bbox_to_anchor=(1., 1.), loc='upper right', numpoints=1, ncol=1)

#Set title
ax.set_title(' A', x=0, y=1, loc='left', weight='bold')

#Save and show figure
figName = 'redChiSq_N.pdf'
plt.savefig(figName, bbox_inches='tight', bbox_extra_artists=(lgd,), facecolor='w', edgecolor=None, dpi=100)
plt.show()



