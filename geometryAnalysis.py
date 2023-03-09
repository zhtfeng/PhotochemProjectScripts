# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:50:31 2023

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
fig = plt.figure(dpi=400,figsize=(12,14))
ax = fig.add_subplot(111, projection='3d')
# ax.set_box_aspect(1)  
# ax.set_xlim((1.5,4.1))
# ax.set_ylim((1.5,4.1))
for i in range(1,3600): # I have 2400 trajs in 2400 folders
    
    # workDir= r'/Users/zhitao/Desktop/ServerFile/NAMD-fromN30-300K/atod-' + str(i)
    workDir= r'D:\Research\DBO\NAMD-fromTS-NEW/atod-' + str(i) # each folder has a name of atod-(number), so this is the path to that folder
    traj = NAMDTraj(workDir+r'/atod-'+str(i)+'.md.xyz') # in the traj folder, there is a file called atod-(number)-md.xyz file
    with open(workDir+r'/productName') as f:
        
        trajname = f.readline()    
    
    if trajname == 'exo':
        

        geomArr = pd.read_csv(workDir+r'/geomData.csv')
        if len(geomArr['Bond1'])< 1000: ax.plot(geomArr['Bond1'],geomArr['Bond3'],len(geomArr['Bond1']),linewidth=0.1)
        
    
    if trajname == 'ze':
    

        geomArr = pd.read_csv(workDir+r'/geomData.csv')
        if len(geomArr['Bond1'])< 1000:ax.plot(geomArr['Bond1'],geomArr['Bond3'],len(geomArr['Bond1']),linewidth=0.1)
        
        # if np.max(geomArr['Bond2']) > 3 and np.max(geomArr['Bond3']) > 3:
            
        #     print(i)