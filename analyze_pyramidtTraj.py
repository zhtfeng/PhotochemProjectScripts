#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:59:25 2022

@author: zhitao
"""

import sys
sys.path.append(r'..')


from Class import class_traj
import matplotlib.pyplot as plt
from Class import class_plot
import numpy as np
import matplotlib
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.markers as mk




# workDir = r'E:\MOLCASREAD\atod-1'


plt.rcParams.update({'font.size':14})


fig = plt.figure(dpi=200,figsize=(24,24))
# ax = fig.add_subplot(projection='3d')
ax = fig.add_subplot()



out1,out2,out3 = 0,0,0
endoNum = 0
exoNum = 0
zz = 0
ze = 0
ee = 0
trajcolorDict = {'zz':'r','ze':'seagreen','ee':'blue','exo':'blueviolet','endo': 'deepskyblue'}
for i in range(1,4): # I have 2400 trajs in 2400 folders
    
    workDir= r'/Users/zhitao/Desktop/ServerFile/NAMD-fromN30-300K/atod-' + str(i)
    # workDir= r'D:\NAMD\atod-' + str(i) # each folder has a name of atod-(number), so this is the path to that folder
    traj = class_traj.NAMDTraj(workDir+r'/atod-'+str(i)+'.md.xyz') # in the traj folder, there is a file called atod-(number)-md.xyz file
    hopPt = traj.getHoppingPoint() # this is for NAMD traj, so you can ignore if it is normal MD
    
    
    
    if hopPt is not None:# this is for NAMD traj, so you can ignore if it is normal MD
        
        distinfo1 = traj.getDistanceArr(0,1) # This is obtaining an array of the distances between atom 1 and atom 2. ASE counts the atoms from 0, be careful
        distinfo2 = traj.getDistanceArr(2,5)
        distinfo3 = traj.getDistanceArr(10,13)
        
        exodist =  traj.getDistanceArr(12,7) # This is for determining the endo and exo of the product if it is BCH
        endodist = traj.getDistanceArr(6,11)

        secondCNbond = traj.getDistanceArr(0, 16)
        completeBreakTime = np.argmax(secondCNbond>1.9)
        dihBreakFirst = traj.getDihedralArr(8,1, 10 ,13)
        dihBreakSecond = traj.getDihedralArr(9,0, 13 ,10)
        time = range(len(distinfo1))
        if distinfo2[-1] > 2.5 : # I am looking at the last point of the traj, if the bond length is smaller than the threshold, then it is hexadiene product, so add 1 on the out1 counter.
            
            # ax.scatter(distinfo1[hopPt],distinfo2[hopPt], distinfo3[hopPt],c='r',s=0.3,alpha=0.8)
            out1 += 1
            dih1 = traj.getDihedralArr(6, 5, 1, 10)[-1]# In hexadiene there are also zz,ee,ze. so we need to look at the dihedral angles. they are in degrees
            dih2 = traj.getDihedralArr(3,2,0,13)[-1]
            productFormTime = np.argmax(distinfo2>2.4)
            if  np.cos(dih1) > 0 and np.cos(dih2) > 0:
                print('HD zz at '+str(i))
                traj.name = 'zz'
                zz += 1 
                
            elif np.cos(dih1) < 0 and np.cos(dih2) < 0:
                traj.name = 'ee'
                print('HD ee at '+str(i))
                ee += 1 
                
            else:
                traj.name = 'ze'
                print('HD ze at '+str(i))
                ze += 1 
            
        elif distinfo3[-1] > 2.5: # this is for another HD product
            
            out2 += 1
            dih1 = traj.getDihedralArr(6, 5, 1, 10)[-1]# In hexadiene there are also zz,ee,ze. so we need to look at the dihedral angles. they are in degrees
            dih2 = traj.getDihedralArr(3,2,0,13)[-1]
            productFormTime = np.argmax(distinfo3>2.4)
            if  np.cos(dih1) > 0 and np.cos(dih2) > 0:
                traj.name = 'zz'
                print('HD zz at '+str(i))
                zz += 1 
                
            elif np.cos(dih1) < 0 and np.cos(dih2) < 0:
                traj.name = 'ee'
                print('HD ee at '+str(i))
                ee += 1 
                
            else:
                traj.name = 'ze'
                print('HD ze at '+str(i))
                ze += 1 
        elif np.min(distinfo1[-100:-1]) < 1.9: # this is looking for minimum bond length, if it is smaller than threshold, it is a ladderene
            # canvas = class_plot.TrajEnsemblePlot().plotTraj3DPolar(ax, distinfo2,dihedralfar,dihedralclose,color='r')
            # ax.scatter(distinfo1[hopPt],distinfo2[hopPt], distinfo3[hopPt],c='r',s=0.3,alpha=0.8)
            productFormTime = np.argmax(distinfo1<1.9)
            out3 += 1
            if exodist[-1] < endodist[-1] :
                # print(endodihedral[-1]*180/np.pi-360)
                traj.name = 'exo'
                print('BCH at '+str(i)+ ' exo')
                exoNum += 1
            else:
                traj.name = 'endo'
                print('BCH at '+str(i)+ ' endo')
                endoNum += 1
                
        if traj.name is not None:
            
            # print(dihBreakFirst)
            color = trajcolorDict[traj.name]
            # ax.plot(np.sin(dihBreakFirst)[0:completeBreakTime],np.sin(dihBreakSecond)[0:completeBreakTime],color=color,linewidth='0.4')
            # ax.plot(np.sin(dihBreakFirst),np.sin(dihBreakSecond),color=color,linewidth='0.4')
            ax.scatter(np.sin(dihBreakSecond)[completeBreakTime],np.sin(dihBreakFirst)[completeBreakTime],c=color,alpha=0.4,s=6)
            ax.scatter(np.sin(dihBreakSecond)[0],np.sin(dihBreakFirst)[0],marker='^',c=color,alpha=0.4,s=6)
            
            ax.plot(np.sin(dihBreakSecond)[completeBreakTime:productFormTime+1],np.sin(dihBreakFirst)[completeBreakTime:productFormTime+1],color=color,linewidth='0.2')
            # ax1.scatter(np.sin(dihBreakFirst)[completeBreakTime],np.sin(dihBreakSecond)[completeBreakTime],c=color,alpha=0.5)
            ax.scatter(np.sin(dihBreakSecond)[productFormTime],np.sin(dihBreakFirst)[productFormTime],c=color,alpha=0.4,marker='*',s=6)
    else:
            
        pass
        
        print('plotting' + str(i))
# line1, = ax.scatter([1],[2],label = '1')
# line2, = ax.plot([1,2,3],label = '2')
# ax.legend([line1,line2],['label1','label2'],labelcolor=['r','g'],bbox_to_anchor=(1.05,1),loc='upper left')
# ax.legend(bbox_to_anchor=(1.05,1),loc='upper left')
handleList = []
fig = plt.figure(dpi=200,figsize=(24,24))
# ax = fig.add_subplot(projection='3d')
ax = fig.add_subplot()
ax.set_xlabel('sin(A)')
ax.set_ylabel('sin(B)')
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_box_aspect(1)
for trajtype,color in trajcolorDict.items():
    
    handleList.append(mlines.Line2D([],[],marker='*',label= trajtype + ' product',linestyle='None',color=color,markersize=4))
    handleList.append( mlines.Line2D([],[],marker='o',label= trajtype + ' diradical',linestyle='None',color=color,markersize=4))
    handleList.append( mlines.Line2D([],[],marker='^',label= trajtype +' TS',linestyle='None',color=color,markersize=4))
    handleList.append( mlines.Line2D([],[],marker=None,label= trajtype +' trajectory',color=color))
    
ax.legend(handles=handleList,bbox_to_anchor=(1.05,1),loc='upper left',prop={'size':8},ncol=2)
plt.subplots_adjust(bottom=0.2)



# print(out1/(out1+out2+out3))
# print(out2/(out1+out2+out3))
# print(out3/(out1+out2+out3))

# print('total reactive   '+ str(out1+out2+out3))
# print('HD1   '+ str(out1))
# print('HD2   '+ str(out2))
# print('BCH   '+ str(out3))

# print('endo:  '+ str(endoNum))

# print('exo:   ' + str(exoNum))


# print('ZZ  ' + str(zz) + '   ' + str(zz/(zz+ze+ee)))
# print('ZE  ' + str(ze) +  '   ' + str(ze/(zz+ze+ee)))
# print('EE  ' + str(ee)  + '   ' + str(ee/(zz+ze+ee)))

plt.show()