# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 14:39:23 2022

@author: 13237
"""

from Class import class_qm
import ase.io

# gvector = class_qm.Multisurface().branchingInitVel('hvector.xyz', 'gvector.xyz',1,37)
gvector = class_qm.Multisurface().branchingInitVel('hvector.xyz', 'gvector.xyz',2,37)
