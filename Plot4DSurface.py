#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:33:46 2022

@author: zhitao
"""

from Class import class_traj
import matplotlib.pyplot as plt
from Class import class_plot
import numpy as np
import matplotlib
import pandas as pd
import matplotlib as mpl
from Class import class_interface
from matplotlib import cm
from matplotlib.ticker import MaxNLocator
# workDir = r'/Users/zhitao/OneDrive - University of California, Davis/Research Projects/Norrish-Cope/Scan/NEB-scan/scan'

totalPECDF = pd.DataFrame(columns=['x','y','z','E'])


# # NEB scan read part
# for i in range(0,18):
    
#     currentDir = workDir+r'/n'+str(i)
#     allxyzfile = currentDir+ r'/scan-neb.allxyz'
#     xyzfile = currentDir+ r'/scan-neb.xyz'

#     class_interface.ORCAInterface().convertAllXYZToXYZ(allxyzfile, xyzfile)
#     traj = class_traj.NAMDTraj(xyzfile)
#     x = traj.getDistanceArr(1,2)
#     y = traj.getDistanceArr(0,3)
#     z = traj.getDistanceArr(4,5)
#     interface = class_interface.ORCAInterface()
#     energy = interface.readDATFileEnergy(currentDir+r'/scan-neb.relaxscanact.dat')
#     tempArray = np.zeros((len(x),4))
#     tempArray[:,0] = x
#     tempArray[:,1] = y
#     tempArray[:,2] = z
#     tempArray[:,3] = energy
    
    
#     tempDF = pd.DataFrame(tempArray,columns=['x','y','z','E'])
#     totalPECDF = totalPECDF.append(tempDF,ignore_index=True)



# cope scan

workDir = r'D:\OneDrive - University of California, Davis\Research Projects\Norrish-Cope\Scan\scan_cope'
allxyzfile = workDir+ r'\scan.allxyz'
xyzfile = workDir+ r'\scan.xyz'


class_interface.ORCAInterface().convertAllXYZToXYZ(allxyzfile, xyzfile)
traj = class_traj.NAMDTraj(xyzfile)
x = traj.getDistanceArr(2,3)
y = traj.getDistanceArr(1,4)
z = traj.getDistanceArr(0,5)
interface = class_interface.ORCAInterface()
energy = interface.readDATFileEnergy(workDir+r'\PT2\scan.xyznevpt2.dat')
tempArray = np.zeros((len(x),4))
tempArray[:,0] = x
tempArray[:,1] = y
tempArray[:,2] = z
tempArray[:,3] = energy


tempDF = pd.DataFrame(tempArray,columns=['x','y','z','E'])
totalPECDF = totalPECDF.append(tempDF,ignore_index=True)

# retro 2+2 scan

# workDir = r'/Users/zhitao/OneDrive - University of California, Davis/Research Projects/Norrish-Cope/Scan/scan-dboboat2D'
workDir = r'D:\OneDrive - University of California, Davis\Research Projects\Norrish-Cope\Scan\Data_Cope_Ladder\Ladder'
# allxyzfile = workDir+ r'/scan-dboboat2D.allxyz'
allxyzfile = workDir+ r'/scan-bond-dbofromBCH.allxyz'

# xyzfile = workDir+ r'/scan-dboboat2D.xyz'
xyzfile = workDir+ r'/scan-bond-dbofromBCH.xyz'

class_interface.ORCAInterface().convertAllXYZToXYZ(allxyzfile, xyzfile)
traj = class_traj.NAMDTraj(xyzfile)
x = traj.getDistanceArr(1,2)
y = traj.getDistanceArr(0,3)
z = traj.getDistanceArr(4,5)
interface = class_interface.ORCAInterface()
# energy = interface.readDATFileEnergy(workDir+r'/scan-dboboat2D.relaxscanact.dat')
energy = interface.readDATFileEnergy(workDir+r'/scan-bond-dbofromBCH.xyznevpt2.dat')
tempArray = np.zeros((len(x),4))
tempArray[:,0] = x
tempArray[:,1] = y
tempArray[:,2] = z
tempArray[:,3] = energy


tempDF = pd.DataFrame(tempArray,columns=['x','y','z','E'])
totalPECDF = totalPECDF.append(tempDF,ignore_index=True)

# plot


totalPECDFcopy = totalPECDF.copy(deep=True)
totalPECDFcopy['x'] = totalPECDF['z']
totalPECDFcopy['z'] = totalPECDF['x']
totalPECDF = totalPECDF.append(totalPECDFcopy,ignore_index=True)
print(totalPECDF)

x = np.array(totalPECDF['x'])
# x = x.reshape((18,30))
y = np.array(totalPECDF['y'])
# y = y.reshape((18,30))
z = np.array(totalPECDF['z'])
# z = z.reshape((18,30))
E = np.array(totalPECDF['E'])
# E = E.reshape((18,30))
E = (E-np.min(E))*627.5


mpl.rc('font',family='arial')
plt.rcParams.update({'font.size': 6})
plt.rcParams['axes.linewidth'] = .2
plt.rcParams['xtick.major.width'] = .2
plt.rcParams['ytick.major.width'] = .2
# plt.rcParams['ztick.major.width'] = .2
plt.rcParams['axes.linewidth'] = .2
plt.rcParams['grid.linewidth'] = .2

# cax = plt.axes([0.85, 0.1, 0.075, 0.8])

fig = plt.figure(dpi=300,figsize=(24,24))
fig.patch.set_facecolor('white')
ax = fig.add_subplot(projection='3d')
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.yaxis.set_major_locator(MaxNLocator(5)) 
ax.xaxis.set_major_locator(MaxNLocator(5))
ax.zaxis.set_major_locator(MaxNLocator(5))
ax.tick_params(labelsize='medium',length=100)
ax.grid(False)


# ax.plot_surface(x,y,E,cmap=matplotlib.cm.coolwarm)
p = ax.scatter(x,y,z,c = E,cmap='rainbow',s=0.2)


# fig.colorbar(p)
totalPECDF.to_csv('PES.csv')



