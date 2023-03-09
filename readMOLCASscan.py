#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 09:19:05 2022

@author: zhitao
"""

from Class import class_interface
import numpy as np
import matplotlib.pyplot as plt
workDir = r'/Users/zhitao/Desktop/ServerFile/scan/'
npoints = 24
nstates = 3
energyArr =  np.zeros([npoints,nstates])

with open(workDir+'total.xyz','w') as file:
    pass

for i in range(0,npoints):
    
    outfile = workDir + 'n'+ str(i)+'/MOLCAS.log'
    outxyzfile = workDir + 'n'+ str(i)+'/MOLCAS.Opt.xyz'
    readmolcas = class_interface.MolcasInterface(18,outfile)

    if readmolcas.checkHappyLanding():
        # energyArr[i] = readmolcas.readMCPDFTOptimizationlog(3)
        energyArr[i] = readmolcas.readCASSCFOptimizationlog(nstates)
    
    else:
        # energyArr[i] = [np.nan,np.nan,np.nan]
        energyArr[i] = readmolcas.readCASSCFOptimizationlog(nstates)
    with open(outxyzfile,'r') as xyzfile:
        xyz = xyzfile.readlines()
        
    with open(workDir+'total.xyz','a') as file:
        
        file.writelines(xyz)
        
print(energyArr)

# plt.plot(energyArr[:,1])
plt.plot(energyArr[:,0])
# plt.plot(energyArr[:,2])