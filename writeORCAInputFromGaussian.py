# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:50:14 2021

@author: Feng
"""

from class_interface import *
import os

workDir = 'D:\\Port\\pummer\\'

folderInfoList = list(os.walk(workDir))

for i in range(len(folderInfoList[0][1])+1):
    for filename in folderInfoList[i][2]:
        
        if filename[-4:] == '.log':
            
            inputname = filename[:-4]
            coord = GaussianInterface().readGeom(workDir + str(filename))
            ORCAInterface().writeORCAInput(coord,workDir+'spe.txt',inputname,workDir)
            print(coord)
            