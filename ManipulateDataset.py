# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 10:45:00 2022

@author: 13237
"""

import pandas as pd
import numpy as np
import csv
import json
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
    
    with open('add.json','w') as f:
        
        f.write(totalDF)

def concatenateJson(file1,file2,atmNum):
    
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
    
    with open('atod2.json','w') as f:
        
        f.write(totalDF)
    

    
    # for i in range(len(truncated)):
        
    #     truncated['nac'][i] = [0.0001/(i+10)]
        
    

    
    # with open('atod.json','w') as f:
        
    #     f.write(truncated[1:-1])
    
# def truncateJson():
    
#         df = pd.read_csv('data.csv')
#         # dfDict = df.to_dict(orient='')
    

# def csvTOjson():
    
#     df = pd.read_csv('data.csv')
#     # dfDict = df.to_dict(orient='')

#     dataDict = {'natom':15, 'nstate': 2, 'nnac': 0, 'nsoc': 0}
#     # print(str(df['xyz'].to_list()).replace('"', ''))
#     dataDict['xyz'] = str(df['xyz'].to_list()).replace('"', '')
#     dataDict['energy'] = str(df['energy'].to_list()).replace('"', '')
#     dataDict['grad'] = str(df['grad'].to_list()).replace('"', '')
#     dataDict['nac'] = str(df['nac'].to_list()).replace('"', '')
#     dataDict['soc'] = str(df['soc'].to_list()).replace('"', '')
    
#     df = pd.DataFrame.from_dict(dataDict,orient='index')
        
#     df[0].to_json('atod.json')
#     with open('atod.json') as f:
        
#         a = str(json.load(f))
#         a = a.replace(': "', ': ')
#         a = a.replace(']\']"',']\']' )
#         print(a)
# truncateJson('New-data1283-21.json',4,19)
concatenateJson('add.json', 'atod.json',19)
# # csvTOjson()