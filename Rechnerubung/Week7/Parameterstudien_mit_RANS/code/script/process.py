#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat June 11 15:15:00 2022

@author: Karan Chodankar
"""
import subprocess as sub

def question():
    # These commands create a list of the Angles of Attack with interactive user input
    print('We will run simulations of the requested AOAs (angle of attacks). Make sure the relevant folders exist')
    n = int(input("\nHow many AOAs would you like to input? max:21\n"))
    print('\nPlease enter each AOA with a space in between (an integer between 0° and 20°)')
    alpha = list(map(int,input("Enter the angles : ").strip().split()))[:n]
    print('\nFolders with the following AOAs are being simulated in the folder data/raw:',alpha)
    return alpha

def runSimulation(alpha):
    for n in alpha:
        # These commands run the simulation for the specified folders
        my_wd = '../../data/raw/AOA_'+str(n)
        filename = './Allrun'
        sub.Popen(filename, cwd=my_wd, shell=True).wait()

def main():
    alpha = question()
    runSimulation(alpha)  # This Function simulates the specified folders

if __name__ == "__main__":
    main()
