#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:56:35 2022

@author: zhitao
"""

import os
import sys
import pandas as pd
import numpy as np
import csv
import json
import shutil

def truncateJson(filename,start,atmNum):
    df = pd.read_json(filename)
    truncated = df[int(start):]
    truncated = truncated.reset_index(drop=True)
    totalDict = {'natom':atmNum, 'nstate': 2, 'nnac': 0, 'nsoc': 0}
    
    totalDict['xyz'] = truncated['xyz'].to_list()    
    totalDict['energy'] = truncated['energy'].to_list()
    totalDict['grad'] = truncated['grad'].to_list()
    totalDict['nac'] = truncated['nac'].to_list()
    totalDict['soc'] = truncated['soc'].to_list()
    
    totalDF = pd.DataFrame.from_dict(totalDict,orient='index')
    totalDF = pd.DataFrame.to_json(totalDF[0])
    
    with open('NewData.json','w') as f:
        
        f.write(totalDF)

def concatenateJson(file1,file2,atmNum,newfilename):
    
    print(file2)
    df1 = pd.read_json(file1)
    df2 = pd.read_json(file2)
    
    totalDict = {'natom':atmNum, 'nstate': 2, 'nnac': 0, 'nsoc': 0}
    
    totalDict['xyz'] = df1['xyz'].to_list() + df2['xyz'].to_list()    
    totalDict['energy'] = df1['energy'].to_list() + df2['energy'].to_list()
    totalDict['grad'] = df1['grad'].to_list() + df2['grad'].to_list()
    totalDict['nac'] = df1['nac'].to_list() + df2['nac'].to_list()
    totalDict['soc'] = df1['soc'].to_list() + df2['soc'].to_list()
    
    totalDF = pd.DataFrame.from_dict(totalDict,orient='index')
    totalDF = pd.DataFrame.to_json(totalDF[0])
    
    with open(newfilename,'w') as f:
        
        f.write(totalDF)

def collectData(startFOlder,endFolder,atmNum):
    

    for i in range(startFOlder,endFolder):
        
        currentFolder = 'n' + str(i)
        print('Working on ' + currentFolder)
        os.chdir(currentFolder)
        
        folderInfoList = list(os.walk(os.getcwd()))
        # first we look for the largest json file in the folder
        largestFile=[0,None]
        
        for j in range(len(folderInfoList[0][1])+1):
            for filename in folderInfoList[j][2]:
                
                if filename[-5:] == '.json' and filename[:8] == 'New-data':
        
                    if os.path.getsize(filename) > largestFile[0]:
                        
                        largestFile[0] = os.path.getsize(filename)
                        largestFile[1] = filename
        
        # print(largestFile[1])
        # truncateJson(largestFile[1], 10, 19)
        
        # then we start to concatenate the json files
        

            
        shutil.copy(largestFile[1], '../Newdata'+str(i) +'.json')
            

            
        os.chdir('..')
        
        
        
collectData(0,26,19)