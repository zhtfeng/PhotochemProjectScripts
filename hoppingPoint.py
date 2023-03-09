# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:43:58 2023

@author: Feng
"""
import matplotlib as mpl
import sys
sys.path.append(r'..')

from Packages.class_traj import NAMDTraj
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
mpl.rc('font',family='arial')
plt.rcParams.update({'font.size': 16})

productName = 'ze'
hopDihArrZE1 = []
hopDihArrZE2 = []
hopDihArrexo1 = []
hopDihArrexo2 = []
for i in range(1,3600): # I have 2400 trajs in 2400 folders
    
    # workDir= r'/Users/zhitao/Desktop/ServerFile/NAMD-fromN30-300K/atod-' + str(i)
    workDir= r'D:\Research\DBO\NAMD-fromTS-NEW/atod-' + str(i) # each folder has a name of atod-(number), so this is the path to that folder
    traj = NAMDTraj(workDir+r'/atod-'+str(i)+'.md.xyz') # in the traj folder, there is a file called atod-(number)-md.xyz file
    with open(workDir+r'/hopPoint') as f:
        
        hopPt = int(f.readline())
        if hopPt <1 or hopPt > 1990: hopPt = None
        # print(hopPt)
        # if hopPt is not None: f.write(str(hopPt))
        # else: f.write(str(0))
        # print('analyzing '+ str(i))
        print(hopPt)
    with open(workDir+r'/productName') as f:
            
        trajname = f.readline()    
        
    if trajname == 'ze' and hopPt is not None:
        
        # hopStrcutre = traj.getFrameXYZ(hopPt)
        geomArr = pd.read_csv(workDir+r'/geomData.csv')
        dih1 = np.sin(geomArr['dih1'][hopPt])
        dih2 = np.sin(geomArr['dih2'][hopPt])
        
        hopDihArrZE1.append(dih1)
        hopDihArrZE2.append(dih2)
        
    if trajname == 'exo' and hopPt is not None:
    
    # hopStrcutre = traj.getFrameXYZ(hopPt)
        geomArr = pd.read_csv(workDir+r'/geomData.csv')
        dih1 = np.sin(geomArr['dih1'][hopPt])
        dih2 = np.sin(geomArr['dih2'][hopPt])
        
        hopDihArrexo1.append(dih1)
        hopDihArrexo2.append(dih2)
        
hopDihArrZE = np.array([hopDihArrZE1,hopDihArrZE2]).T
hopDihArrexo = np.array([hopDihArrexo1,hopDihArrexo2]).T
# hist2D = np.histogram2d(hopDihArr[:,0], hopDihArr[:,1],bins=[25,25])[0]
    
# print(hopDihArr)
fig, ax = plt.subplots(nrows=1, ncols=1)
ax.set_xlabel('sin(A)')
ax.set_ylabel('sin(B)')  

ax.set_box_aspect(1)          
# meshplot = ax.hist2d(hopDihArrZE[:,0],hopDihArrZE[:,1],cmap='hot',bins=[50,50])
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)  
meshplot = ax.hist2d(hopDihArrexo[:,0],hopDihArrexo[:,1],cmap='hot',bins=[50,50])