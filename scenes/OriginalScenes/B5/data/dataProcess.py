import numpy as np
import os

pathread = r'/home/owen/Softwares/ext_plugin_repo/SoftRobots/Simulation/Ex1/'

os.chdir(pathread)
a = np.loadtxt('tetras_x.txt')
t = np.array(a[:,0]).reshape(len(a[:,1]),1)

nrow = 24
X = []; Y = []; Z = []
for j in range(0, nrow):                  # j is rows
    for i in range(1, len(a[1,:])):     # i means columns
        if((i-1) % 3 == 0):
            X = np.append(X, a[j,i])
        #if((i-2) % 3 == 0):
       #     Y = np.append(Y, a[j,i])
       # if((i-3) % 3 == 0):
      #      Z = np.append(Z, a[j,i])
for j in range(0, len(X)):
        X = X.reshape(nrow, 10450)
np.savetxt('OwenX.txt', X, fmt='%1.3f')
