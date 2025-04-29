#!python
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os, glob
import seaborn as sns

# OUTPUT 
# is the time that each unique mol stay inside the solvation shell of the reference molecule. it doesn't take into account exit and reanter of the molecule. It just count the percentage of frames in qhich the observed molecule is in the solvation shell of the reference molecule.

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

#Number of Frames for each molecule
MOL1 = []
MOL2 = []
# Time in ps between the frames of trajectory
DT=60

frames = 1
for filename in glob.glob('1_*.log'):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        dati = pd.read_csv(filename,header=None)
        dati = dati[0].str.split(' ', expand=True)
        unici = dati.stack().unique()
        tmp = [ dati.isin([i]).sum().sum()  for i in unici ]
        MOL1 = np.append(MOL1, tmp)
        frames = frames + 1


for filename in glob.glob('2_*.log'):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        dati = pd.read_csv(filename,header=None)
        dati = dati[0].str.split(' ', expand=True)
        unici = dati.stack().unique()
        tmp = [ dati.isin([i]).sum().sum()  for i in unici ]
        MOL2 = np.append(MOL2, tmp)

#every frame is between 25ps
#AL2=AL2*25/1000 #ns
#AL4=AL4*25/1000 #ns
MOL1 = MOL1*DT
MOL2 = MOL2*DT

print(MOL1)
print(MOL2)

sns.set_style("white")
plt.figure(dpi= 300)
#sns.distplot(MOL1, color="dodgerblue", label="MOL1")

plt.hist([MOL1,MOL2],density=True, bins=20, histtype='bar', color=[PURPLE,GRAY], label=[r'[AlCl$_2$]$^+$','[AlCl$_4$]$^-$'])

plt.legend()

plt.xlabel(r'residency time / ps')
plt.ylabel(r'probability density')
#plt.savefig(r'../plot.png')
plt.show()
