#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:48:59 2022

@author: zhitao
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


mpl.rc('font',family='arial')
plt.rcParams.update({'font.size': 16})

def plot_dihedral(start,end,i,trajName):
    
    
        
    fig, ax = plt.subplots(nrows=1, ncols=1)
    # ani = animation.FuncAnimation(fig, animate, frames=2)
    
    # ani.save('test.gif', writer='Pillow')
    # index1DArr = np.array(range(10))

    
    ax.set_xlabel('sin(A)')
    ax.set_ylabel('sin(B)')
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_box_aspect(1)
    
    # timeFrameList = t
    # timeFrameList = range(0,200,40)
    # for i,j in enumerate(timeFrameList):
    #     tot_slice_List.append(tot_dihedral_array)
        
    timingList = []
    tot_dihedral_array = np.array([[0,0]])
    # for t in timeFrameList:
    for traj in range(start,end):
        # print(traj)
        # workDir = r'/Users/zhitao/Desktop/ServerFile/NAMD-fromTS-NEW/atod-' + str(traj)+r'/' 
        workDir = r'D:\Research\DBO\NAMD-fromTS-NEWatod-' + str(traj)+r'/'
        with open(workDir+r'productName') as f:
            
            trajname = f.readline()
            
        if trajname == trajName:
            
            geomArr = pd.read_csv(workDir+r'geomData.csv')
            dih1 = np.sin(geomArr['dihskeleton1'])
            dih2 = np.sin(geomArr['dihskeleton2'])
            # dih1 = np.gradient(geomArr['dihskeleton1'])
            # dih2 = np.gradient(geomArr['dihskeleton2'])
            # dih1 = geomArr['dihskeleton1']
            # dih2 = geomArr['dihskeleton2']
            dihArrCurrentTraj = np.zeros((len(dih1),2))
            dihArrCurrentTraj[:,0] = dih1
            dihArrCurrentTraj[:,1] = dih2
            
            if trajname == 'exo' or trajname == 'endo': 
                
                productFormTime = np.argmax(geomArr['Bond1']<2.0)
                cnDiradicalFormTime = np.argmax(geomArr['secondCNBond']>2.8)
                
            elif trajname == 'zz' or trajname == 'ze' or trajname == 'ee':
                
                productFormTime = np.max([np.argmax(geomArr['Bond2']>2),np.argmax(geomArr['Bond3']>2)])
                cnDiradicalFormTime = np.argmax(geomArr['secondCNBond']>2.8)
                dihArrCurrentTraj = dihArrCurrentTraj[0:productFormTime,:]
                # print(productFormTime)
                # if productFormTime  < 1000:
            timingList.append(cnDiradicalFormTime)
                    # tot_dihedral_array = np.concatenate((tot_dihedral_array, dihArrCurrentTraj[productFormTime-100:productFormTime-50,:]),axis=0)
            
                                
            if (i+1)*20 < productFormTime and productFormTime < 600: 
            
                     tot_dihedral_array = np.concatenate((tot_dihedral_array, dihArrCurrentTraj[i*20:(i+1)*20,:]),axis=0)
    
    # hexbin = ax.hexbin(tot_dihedral_array[:,0],tot_dihedral_array[:,1],cmap='inferno',gridsize=(20,20),norm=matplotlib.colors.Normalize(vmin = 0,vmax=200))
    # print(hexbin[0])
    hexbin = ax.hist2d(tot_dihedral_array[:,0],tot_dihedral_array[:,1],cmap='inferno',density=True,bins=[30,30])
    return hexbin
    # fig.colorbar(hexbin)
    # fig.savefig(r'D:\Photochem\fig\\' +str(i)+ '.png')
    # fig.savefig(r'/Users/zhitao/Desktop/ServerFile/Figures/BCH/' +str(i)+ '.png')
    
    # fig = plt.figure() 
    # ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1)) 
    
    # fig, ax = plt.subplots(nrows=1, ncols=1)

    # # ani = animation.FuncAnimation(fig, animate, frames=2)
    
    # # ani.save('test.gif', writer='Pillow')
    # # index1DArr = np.array(range(10))

    
    # ax.set_xlabel('sin(A)')
    # ax.set_ylabel('sin(B)')
    # ax.set_xlim(-1,1)
    # ax.set_ylim(-1,1)
    # ax.set_box_aspect(1)
    
    # for i in range(5):
                    
    #     axs[i].hexbin(tot_slice_List[i][:,0],tot_slice_List[i][:,1],cmap='inferno')
    #     axs[i].set_box_aspect(1)
    # # ax1.hist(timingList,bins=40)
    # plt.subplots_adjust(bottom=0.2)

def generatehist2D(start,end,i,trajName):
    

        
    timingList = []
    tot_dihedral_array = np.array([[0,0]])
    # for t in timeFrameList:
    for traj in range(start,end):
        # print(traj)
        # workDir = r'/Users/zhitao/Desktop/ServerFile/NAMD-fromTS-NEW/atod-' + str(traj)+r'/'
        workDir = r'D:\Research\DBO\NAMD-fromTS-NEW\atod-' + str(traj)+r'/'
        with open(workDir+r'productName') as f:
            
            trajname = f.readline()
            
        if trajname == trajName:
            
            geomArr = pd.read_csv(workDir+r'geomData.csv')
            dih1 = np.sin(geomArr['dihskeleton1'])
            dih2 = np.sin(geomArr['dihskeleton2'])
            
            # dih1 = np.gradient(geomArr['dihskeleton1'])
            # dih2 = np.gradient(geomArr['dihskeleton2'])
            
            # dih1 = geomArr['dihskeleton1']
            # dih2 = geomArr['dihskeleton2']
            dihArrCurrentTraj = np.zeros((len(dih1),2))
            dihArrCurrentTraj[:,0] = dih1
            dihArrCurrentTraj[:,1] = dih2
            
            if trajname == 'exo' or trajname == 'endo': 
                
                productFormTime = np.argmax(geomArr['Bond1']<2.0)
            #     cnDiradicalFormTime = np.argmax(geomArr['secondCNBond']>2.8)
                
            elif trajname == 'zz' or trajname == 'ze' or trajname == 'ee':
                
                productFormTime = np.max([np.argmax(geomArr['Bond2']>2),np.argmax(geomArr['Bond3']>2)])
                # cnDiradicalFormTime = np.argmax(geomArr['secondCNBond']>2.8)
                # dihArrCurrentTraj = dihArrCurrentTraj[0:productFormTime,:]
                # print(productFormTime)
                # if productFormTime  < 1000:
            # timingList.append(cnDiradicalFormTime)
                    # tot_dihedral_array = np.concatenate((tot_dihedral_array, dihArrCurrentTraj[productFormTime-100:productFormTime-50,:]),axis=0)
            
                                
            if productFormTime < 600: 
            
                tot_dihedral_array = np.concatenate((tot_dihedral_array, dihArrCurrentTraj[15*i:15*(i)+5,:]),axis=0)
    
    # hexbin = ax.hexbin(tot_dihedral_array[:,0],tot_dihedral_array[:,1],cmap='inferno',gridsize=(20,20),norm=matplotlib.colors.Normalize(vmin = 0,vmax=200))
    # print(hexbin[0])
    hexbin = np.histogram2d(tot_dihedral_array[:,0],tot_dihedral_array[:,1],bins=[25,25])[0]/np.shape(tot_dihedral_array)[0]
    # print(hexbin)
    return hexbin



def scaleHistDiff(hist1,hist2):
    
    hist_diff = hist1-hist2
    hist_diff_min = np.ones_like(hist1) * np.min(hist_diff)
    data = 2*(hist_diff-hist_diff_min)/(np.max(hist_diff)-np.min(hist_diff))-1
    center  = 2*(0-np.min(hist_diff))/(np.max(hist_diff)-np.min(hist_diff))-1
    
    return data,center


    
    
trajcolorDict = {'zz':'r','ze':'seagreen','ee':'blue','exo':'blueviolet','endo': 'deepskyblue'}

for i in np.arange(0,40,1):
    
    fig, ax = plt.subplots(nrows=1, ncols=1,dpi=400)   
    ax.set_xlabel('sin(A)')
    ax.set_ylabel('sin(B)')
    # ax.set_xlim(-1,1)
    # ax.set_ylim(-1,1)
    ax.set_box_aspect(1)
    print('plotting '+ str(i))

    hist1 = generatehist2D(1,3601,i,'ze')
    hist2 = generatehist2D(1, 3601, i, 'exo')
    x = np.arange(-1, 1.08,0.08)  # len = 11
    y = np.arange(-1, 1.08,0.08)  # len = 7
    X, Y = np.meshgrid(x, y)
    print(X)
    data,center = scaleHistDiff(hist1, hist2)
    print(data)
    norm = mpl.colors.TwoSlopeNorm(vcenter=center)
    meshplot = ax.pcolormesh(X,Y,data,cmap='seismic',norm=norm)
    # plt.colorbar(meshplot)
    
    # norm = matplotlib.colors.TwoSlopeNorm(vmin=center)
    # x = np.arange(-1,1,.08)
    # y = np.arange(-1,1,.08)
    # X,Y = np.meshgrid(x,y)
    # meshplot = ax.pcolormesh(X,Y,hist2,cmap='Blues')
    # plt.colorbar(meshplot)
    
    # fig.savefig(r'D:\Photochem\fig\\' +str(i)+ '.png')
    fig.savefig(r'D:\Research\DBO\Figures\fig' +str(i)+ '.png')
    
    
