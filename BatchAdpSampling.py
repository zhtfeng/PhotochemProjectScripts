#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 11:10:36 2022

@author: zhitao
"""

from Class import class_traj
from Class import class_interface
import os
import shutil

# test = class_traj.Traj('output.xyz').writexyzBohr()

# newmolden = class_interface.MoldenInterface('atod.freq.molden').replaceCoord(test[0])

# with open('new.molden','w') as f:
    
#     f.writelines(newmolden)
    
    
def write_adaptive_input(xyzFile):
    
    xyz = class_traj.Traj(xyzFile).xyz
    
    for i in range(len(xyz)):
        
        currentDir=r'D:\MolcasRead\n'+str(i)
        
        if os.path.isdir(currentDir): 
            shutil.rmtree(currentDir)
            
        shutil.copytree(r'D:\MolcasRead\SOC', currentDir)
        os.chdir(currentDir)
        xyz[i].write('freq.xyz')
        # shutil.copytree(r'D:\MolcasRead\adaptive', currentDir)
        # os.chdir(currentDir)
        # newmolden = class_interface.MoldenInterface(r'D:\MolcasRead\atod.freq.molden').replaceCoord(xyz[i])
        
        
        # with open('atod.freq.molden','w') as f:
        
        #     f.writelines(newmolden)
        #     f.close()
            
    os.chdir('..')
            
            


write_adaptive_input(r'D:\MolcasRead\output.xyz')