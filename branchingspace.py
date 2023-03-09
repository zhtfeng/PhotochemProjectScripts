# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 00:23:41 2022

@author: 13237
"""

from Class import class_interface
from Class import class_plot



def generate_bracningspcase_XYZ():
    
    interface = class_interface.MolcasInterface()
    interface.writeBranchingSpace_to_allXYZ('MOLCAS.Opt.xyz', 'hvector.xyz', 'gvector.xyz', 0.1,6)


generate_bracningspcase_XYZ()    
class_plot.PlotSurface.branchingSurface('CHT-branchingSpace.xlsx')


