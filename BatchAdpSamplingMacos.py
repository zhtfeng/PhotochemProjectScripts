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
import ase
# test = class_traj.Traj('output.xyz').writexyzBohr()

# newmolden = class_interface.MoldenInterface('atod.freq.molden').replaceCoord(test[0])

# with open('new.molden','w') as f:
    
#     f.writelines(newmolden)
    
    
def write_adaptive_input(xyzFile):
    
    # xyz = class_traj.Traj(xyzFile).writexyzBohr()
    xyz = class_traj.Traj(xyzFile).xyz
    
    
    
    for i in range(len(xyz)):
        
        currentDir=r'/Users/zhitao/OneDrive - University of California, Davis/Research Projects/Norrish-Cope/NEBscan/n'+str(i)
        
        if os.path.isdir(currentDir): 
            shutil.rmtree(currentDir)
        
        # shutil.copytree(r'/Users/zhitao/OneDrive - University of California, Davis/Coding Project/Pydyn/adaptive', currentDir)
        shutil.copytree(r'/Users/zhitao/OneDrive - University of California, Davis/Research Projects/Norrish-Cope/NEBscan/template/', currentDir)
        os.chdir(currentDir)
        xyz[i].write('file.xyz')
        # newmolden = class_interface.MoldenInterface(r'/Users/zhitao/OneDrive - University of California, Davis/Coding Project/Pydyn/atod.freq.molden').replaceCoord(xyz[i])
        
        # with open('atod.freq.molden','w') as f:
        
        #     f.writelines(newmolden)
        



write_adaptive_input(r'/Users/zhitao/OneDrive - University of California, Davis/Research Projects/Norrish-Cope/NEBscan/neb_MEP_trj.xyz')