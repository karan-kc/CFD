#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat June 11 15:15:00 2022

@author: Karan Chodankar
"""

u_bulk = 1.3452
rho = 1.225
re = 18000

def get_Tau(shearStressFile):
    notLine = ''
    tau = None
    for notLine in open(shearStressFile,'r'):
        li=notLine.strip()
        if not li.startswith("#"):
            line = notLine.rstrip()
            temp1 = line.split("(")[2]
            tau = float(temp1.split(' ')[0])
    return abs(tau)

def main():
    """
    this is the function used to call all functions necessary for the task
    """

    shearStressFile = './postProcessing/wallShearStress/0/wallShearStress.dat'
    tau = get_Tau(shearStressFile)   # Magnitude of Maximum Wall Shear Stress is taken from postProcessing at top-Wall

    c_f = tau / (0.5 * rho * u_bulk ** 2)
    c_f_dean = 0.073 * re ** (-1 / 4)
    dev = abs((c_f - c_f_dean) / c_f_dean)  # The Deviation is about 12%

    print("The deviation from the Dean-Correlation is "+str(dev*100)+"%")

###############################################################################
if __name__ == "__main__":
    main()
