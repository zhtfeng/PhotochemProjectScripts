import numpy as np
import os
import re
import pandas as pd
import sys

class Initcond:

    def __init__(self,atomNum,filename='initconds'):
        self.atomNum = atomNum
        self.filename = filename
        self.indexNumList = self.getIndexPoint()


    def openFile(self):

        file = open(self.filename)
        readfile = file.readlines()
        file.close()
        return readfile

    def getIndexPoint(self):

        file = self.openFile()
        indexNumList = []
        for lineNum,line in enumerate(file):
            if line[:5] == 'Index':
                indexNumList.append(lineNum)

        return indexNumList

    def parse(self, num,reverse=False):

        file = self.openFile()
        num = self.indexNumList[num]
        CoordArr = [file[i] for i in range(num+2,num+2+self.atomNum)]

        SumFile = []

        for i in CoordArr:
            line = re.split(r'[\s]',i)
            while '' in line: line.remove('')
            SumFile.append(line)
        df = pd.DataFrame(SumFile,columns=list('ABCDEFGHI'))
        coord = df.loc[:,list('ABCDEF')]
        coord.to_csv('geom',header=None, index=None, sep=' ', mode='w')
        if not reverse:
            vel = df.loc[:,list('GHI')]
            vel.to_csv('veloc',header=None, index=None, sep=' ', mode='w')
        else:
            vel = df.loc[:,list('GHI')]
            vel = vel.to_numpy().astype(np.float)
            vel = -vel
            np.savetxt("veloc", vel, delimiter=" ")
            
            
class Main():
    
    def __init__(self,sharcFileDir,workDir,numAtom,start,end):
        
        self.sharcFileDir = sharcFileDir
        self.workDir = workDir
        self.numAtom = numAtom
        self.start = start
        self.end = end
    
    
    def set_up_both_direction(self):
        
        trajFolderStart = 0
        trajFolderEnd = 20
        os.chdir('/home/zhtfeng/photochem/denitro/DYN-MOLCAS')
        for i in range(trajFolderStart,trajFolderEnd):
        
            currentFolder = 'n' + str(i)
            print(currentFolder)
            os.system('mkdir ' + currentFolder)
            os.system('cp -RT /home/zhtfeng/photochem/denitro/DynPreparation/ ' + currentFolder +'/forward')
            os.system('cp -RT /home/zhtfeng/photochem/denitro/DynPreparation/ ' + currentFolder + '/backward')
        
            os.chdir(currentFolder)
            os.chdir('forward')
            init = Initcond(15)
            init.parse(i)
            os.chdir('..')
            os.chdir('backward')
            init = Initcond(15)
            init.parse(i, reverse=True)
            os.chdir('..')
            os.chdir('..')
            
    def set_up_both_directionFromInitcond(self):
        
        pass
            
    def set_up_one_direction(self):
        

        os.chdir(self.workDir)
        
        for i in range(self.start,self.end):
            
            trajFolder = 'n' + str(i)
            print(trajFolder)
            isDir = os.path.isdir(trajFolder)
            print(isDir)
            if not isDir:
                os.system('mkdir ' + trajFolder)
            
            os.system('cp -rRT ' + str(self.sharcFileDir) + ' '+ trajFolder)
            os.chdir(trajFolder)
            
            
    def set_up_random(self):
        
        os.chdir(self.workDir)
        
        for i in range(int(self.start),int(self.end)):
            
            trajFolder = 'n' + str(i)
            print(trajFolder)
            isDir = os.path.isdir(trajFolder)
            print(isDir)
            if not isDir:
                os.system('mkdir ' + trajFolder)
            os.system('cp -RT ' + str(self.sharcFileDir) + ' '+ trajFolder)
            os.chdir(trajFolder)
            with open('input','a') as inputfile:
                
                inputfile.write('\n rngseed '+ str(i+1)+'\n')
            
            os.chdir('..')
            
            
            
            
print(sys.argv)
_,sharcDir,workdir,atomnum,start,end = sys.argv

setup = Main(sharcDir,workdir,atomnum,start,end)

setup.set_up_random()
            
    
    
    
    
    
    
    