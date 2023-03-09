# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 01:10:32 2022

@author: 13237
"""

from Class import class_interface
import os

def getAllJson():
    
    start=0
    for i in range(0,3):       
        
        # os.chdir(r'./MolcasOut/n'+str(i))
        os.chdir(r'/Users/zhitao/OneDrive - University of California, Davis/Coding Project/Pydyn/NAMD/')
        out = class_interface.MolcasInterface(18,'MOLCAS.log')
        start = out.getPyramidJsonData(start,saveDir=r'/Users/zhitao/OneDrive - University of California, Davis/Coding Project/Pydyn/NAMD/')
        os.chdir(r'..')
        os.chdir(r'..')
    # out.compileJsonDataFile(1595)
        
getAllJson()
out = class_interface.MolcasInterface(18,r'/Users/zhitao/OneDrive - University of California, Davis/Coding Project/Pydyn/NAMD/MOLCAS.log')
out.compileJsonDataFile(2,r'/Users/zhitao/OneDrive - University of California, Davis/Coding Project/Pydyn/NAMD')