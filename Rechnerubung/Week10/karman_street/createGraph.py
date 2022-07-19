#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat June 11 15:15:00 2022

@author: Karan Chodankar
"""
import matplotlib.pyplot as mpl

class simData(object):
    pass

def readresults():
    """
    This function reads the output file of a simulation
    """
    # Datenobjekt definieren
    data = simData()
    data.cd = []
    data.cl = []

    notLine = ''
    for notLine in open('./postProcessing/forceCoeffs_object/0/forceCoeffs.dat','r'):
        li=notLine.strip()
        if not li.startswith("#"):
            line = notLine.rstrip()
            data.cd.append(float(line.split("\t")[2]))
            data.cl.append(float(line.split("\t")[3]))
    mpl.figure(num=1, dpi=500)
    mpl.plot(data.cd, data.cl, 'g-', label='Lilienthal Polar')
    mpl.xlabel('$c_{d}, [-]$')
    mpl.ylabel('$c_{l}, [-]$')
    # Legende aktivieren
    mpl.legend()
    # Abspeichern als PNG
    mpl.tight_layout()
    mpl.savefig('./plot.png', format="png")

def main():
    """
    this is the function used to call all functions necessary for the task
    """
    data = readresults()

if __name__ == "__main__":
    main()
