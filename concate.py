#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:02:19 2022

@author: zhitao
"""

import os
import sys
import pandas as pd
import numpy as np
import csv
import json
import shutil

def truncateJson(filename,start,atmNum,newfilename):
    print(filename)
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
    
    with open(newfilename,'w') as f:
        
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

for i in range(0,26):
    
    atmNum = 19
    if i == 0:
        
        truncateJson('./data/Newdata'+'0'+'.json', 10, atmNum,'./tmp/truncData'+'0'+'.json')
        
    elif i ==1:
        
        truncateJson('./data/Newdata'+'1'+'.json', 10, atmNum,'./tmp/truncData'+'1'+'.json')
        concatenateJson('./tmp/truncData'+'0'+'.json', './tmp/truncData'+'1'+'.json', atmNum, './tmp/concatData1.json')
        
    else:
        
        truncateJson('./data/Newdata'+str(i)+'.json', 10, atmNum,'./tmp/truncData'+str(i)+'.json')
        concatenateJson('./tmp/concatData'+str(i-1)+'.json', './tmp/truncData'+str(i)+'.json', atmNum, './tmp/concatData'+str(i)+'.json')
    
    