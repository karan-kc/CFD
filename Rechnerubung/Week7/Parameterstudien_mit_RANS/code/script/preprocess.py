#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat June 11 15:15:00 2022

@author: Karan Chodankar
"""
import shutil
import re
import os
import subprocess as sub

def copyDirectory(alpha):
    # These commands clear the raw directory so no conflicts in copying with shutil occur
    shutil.rmtree('../../data/raw', ignore_errors=True)
    os.mkdir('../../data/raw')
    for n in alpha:
        # These commands copy the template folder from code into raw and apply the naming convention
        shutil.copytree('../template', '../../data/raw/template')
        shutil.move('../../data/raw/template', '../../data/raw/AOA_'+str(n))
        with open('../../data/raw/AOA_'+str(n)+'/system/globalVariables', 'r+') as fout:
            # These commands replace the Angle of Attack
            text = fout.read()
            text = re.sub(r'alpha_DEG \t\(float\).*?;',r'alpha_DEG \t(float)'+str(n)+';',text)
            fout.seek(0)
            fout.write(text)
            fout.truncate()
        # These commands run the simulation for the specified folders
        my_wd = '../../data/raw/AOA_'+str(n)                # Comment this line out if you don't want to simulate
        filename = './Allrun'                               # Comment this line out if you don't want to simulate
        sub.Popen(filename, cwd=my_wd, shell=True).wait()   # Comment this line out if you don't want to simulate

def question():
    # These commands create a list of the Angles of Attack with interactive user input
    print('Hello, we will be creating copies of the template folder with the requested AOAs (angle of attacks).')
    n = int(input("\nHow many AOAs would you like to input? max:21\n"))
    print('\nPlease enter each AOA with a space in between (an integer between 0° and 20°)')
    alpha = list(map(int,input("Enter the angles : ").strip().split()))[:n]
    print('\nFolders with the following AOAs are being created and simulated in the folder data/raw:',alpha)
    return alpha

def main():
    alpha = question()
    copyDirectory(alpha)  # This Function can copy the directory, edit the angle, and simulate the folders

if __name__ == "__main__":
    main()





