#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:53:34 2022

@author: zhitao
"""

from Class import class_interface


gaussianinterface = class_interface.GaussianInterface()
gaussianinterface.readIRCLQA("Boat_closure_TS_IRC.log")
gaussianinterface.coordList_to_xyz('irc.xyz')
