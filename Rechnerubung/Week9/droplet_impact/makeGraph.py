#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 7.5.22

@author: Karan Chodankar
"""

###########################################################################
# Importing libraries
###########################################################################

import numpy as np
import matplotlib.pyplot as mpl 
 
# open the file in read mode
fileDir = './postProcessing/swakExpression_beta/0/beta'
time=[]
beta=[]

with open(fileDir) as fin:  #Define object fin as the data source
    # Read the rows from the file
    dataLines = fin.readlines()
    # Trim object to the values of interest
    dataLines=dataLines[1:1500]
    
    # Organize the input data
    dataSplit=[]
    for dataVar in dataLines:
        #Split data into its values and return the result
        dataVar=dataVar.split()
        time.append(float(dataVar[0]))
        beta.append(float(dataVar[1]))
        
#Plot a figure with the main curvatures
mpl.figure(1)
mpl.plot(time,beta)
mpl.xlabel("Time [s]")
mpl.ylabel("Beta (D/D_0)")
mpl.title("Wetting of the lower substrate")
mpl.savefig('./beta.png', format="png")