#!python
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os, glob
import seaborn as sns


from pylab import cm
cmap = cm.get_cmap('tab10',8)
colors=[]
for i in range(cmap.N):
    rgba = cmap(i)
    colors.append(matplotlib.colors.rgb2hex(rgba))
BLUE=colors[0]
GRAY=colors[7]
PURPLE="#EE9BCA"
PINK=colors[6]
RED=colors[3]
ORANGE=colors[1]
GREEN=colors[2]


AL2 = []
AL4 = []
for filename in glob.glob('2_*.out'):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        dati = pd.read_csv(filename,header=None)
        dati2 = dati[0].str.split(' ', expand=True)
        unici = dati2.stack().unique()
        tmp = [ dati2.isin([i]).sum().sum()  for i in unici ]
        AL2 = np.append(AL2, tmp)

for filename in glob.glob('4_*.out'):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        dati = pd.read_csv(filename,header=None)
        dati2 = dati[0].str.split(' ', expand=True)
        unici = dati2.stack().unique()
        tmp = [ dati2.isin([i]).sum().sum()  for i in unici ]
        AL4 = np.append(AL4, tmp)

#every frame is between 25ps
AL2=AL2*25/1000 #ns
AL4=AL4*25/1000 #ns

sns.set_style("white")
plt.figure(dpi= 300)
sns.distplot(AL2, color="dodgerblue", label="Al2")

#plt.hist([AL2,AL4],density=True, bins=10, histtype='bar', color=[PURPLE,GRAY], label=[r'[AlCl$_2$]$^+$','[AlCl$_4$]$^-$'])
plt.legend()
#plt.xlabel(r'residency time / ns')
#plt.ylabel(r'probability density')
#plt.savefig(r'../plot.png')
plt.show()
