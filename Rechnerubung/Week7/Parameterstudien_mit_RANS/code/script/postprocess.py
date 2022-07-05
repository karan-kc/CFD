#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat June 11 15:15:00 2022

@author: Karan Chodankar
"""
import shutil
import matplotlib.pyplot as mpl
import os

class simData(object):
    pass

def question():
    # These commands create a list of the AOA (Angles of Attack) with interactive user input
    print('We will create Lilienthal polars of the requested AOAs. Make sure the relevant AOA folders exist')
    n = int(input("\nHow many AOAs would you like to input? max:21\n"))
    print('\nPlease enter each AOA with a space in between (an integer between 0° and 20°)')
    alpha = list(map(int,input("Enter the angles : ").strip().split()))[:n]
    print('\nLilienthal polars are being graphed for following AOAs within data/processed:',alpha)
    return alpha


def readresults(alpha):
    """
    This function reads the output file of a simulation
    """
    # Datenobjekt definieren
    shutil.rmtree('../../data/processed', ignore_errors=True)
    os.mkdir('../../data/processed')
    data = simData()
    data.cd = []
    data.cl = []

    for n in alpha:
        notLine = ''
        data.cd.clear()
        data.cl.clear()
        for notLine in open('../../data/raw/AOA_'+str(n)+'/postProcessing/forceCoeffs_object/0/forceCoeffs.dat','r'):
            li=notLine.strip()
            if not li.startswith("#"):
                line = notLine.rstrip()
                data.cd.append(float(line.split("\t")[2]))
                data.cl.append(float(line.split("\t")[3]))
        mpl.figure(num=alpha.index(n), dpi=500)
        mpl.plot(data.cd, data.cl, 'g-', label='Lilienthal Polar at AOA '+str(n)+'°')
        mpl.xlabel('$c_{d}, [-]$')
        mpl.ylabel('$c_{l}, [-]$')
        # Legende aktivieren
        mpl.legend()
        # Abspeichern als PNG
        mpl.tight_layout()
        mpl.savefig('../../data/processed/Lilienthal_'+str(n)+'.png',format="png")
        mpl.figure().clear()
        mpl.close()
        mpl.cla()
        mpl.clf()

def main():
    """
    this is the function used to call all functions necessary for the task
    """

    alpha = question()

    data = readresults(alpha)

if __name__ == "__main__":
    main()
