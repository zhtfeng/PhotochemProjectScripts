import os
import sys
    
class Main():
    
    def __init__(self,rootDir,start,end):
        
        self.workRootDir = rootDir
        self.start = int(start)
        self.end = int(end)
    def submit_both_direction(self):
        
        os.chdir(self.workRootDir)
        for i in range(startFolder,endFolder):

            currentFolder = 'n' + str(i)
            print('start submiting ' + currentFolder)
            os.chdir(currentFolder)
            os.chdir('forward')
            os.system('qsub sharcjob_molcas')
            print('Submitted ' + currentFolder + ' forward ' )
            os.chdir('..')
            os.chdir('backward')
            os.system('qsub sharcjob_molcas')
            print('Submitted ' + currentFolder + ' backward ')
            os.chdir('..')
            os.chdir('..')
            
        
    def submit_one_direction(self):
        
        os.chdir(self.workRootDir)

        for i in range(self.start,self.end):

            currentFolder = 'n' + str(i)
            print('start submiting ' + currentFolder)
            os.chdir(currentFolder)
            os.system('sbatch testexpance.run')
            print('Submitted ' + currentFolder)
            os.chdir('..')

_,rootDir,start,end = sys.argv
main = Main(rootDir,start,end)
main.submit_one_direction()