#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat June 11 15:15:00 2022

@author: Karan Chodankar
"""

import matplotlib.pyplot as mpl
import numpy as np
import re


class simData(object):
    pass

def getIterations():
    with open('./log','r') as fout:
        text = fout.read()
        result = re.search('SIMPLE solution converged in (.*) iterations', text)
    return result.group(1)

def readUresults(foldername, iterations):
    """
    This function reads the output file of a simulation
    """
    # Datenobjekt definieren
    u_data = simData()
    u_data.x_01 = []
    u_data.y_01 = []
    u_data.x_05 = []
    u_data.y_05 = []
    u_data.x_09 = []
    u_data.y_09 = []


    with open(foldername+'postProcessing/sample/'+iterations+'/x_by_H_01_U.xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variablen abspeichern (1. und 2. Spalte)
            u_data.x_01.append(float(split_line[1]))
            u_data.y_01.append(float(split_line[0]))
    # TKE einlesen
    with open(foldername+'postProcessing/sample/'+iterations+'/x_by_H_05_U.xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variable abspeichern (2. Spalte)
            u_data.x_05.append(float(split_line[1]))
            u_data.y_05.append(float(split_line[0]))
    # Reynolds-Spannungen einlesen
    with open(foldername+'postProcessing/sample/'+iterations+'/x_by_H_09_U.xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variable abspeichern (3. Spalte)
            u_data.x_09.append(float(split_line[1]))
            u_data.y_09.append(float(split_line[0]))
    # Datenobjekt zurückgeben
    return u_data

def u_x(y, u_inlet, H):
    u_max = (3/2)*u_inlet
    return u_max*(((4*y)/H)-((4*(y**2))/(H**2)))


def plotData(u_data, foldertosave):
    """
    This function plots the data given data object
    """
    u_inlet = 1.85
    H = 0.2

    ylist = np.linspace(0,0.2,num=1000)
    u_x_list = u_x(ylist, u_inlet, H)

    # Scaled Lists:
    U_data = simData()
    U_data.x_01 = [i/u_inlet for i in u_data.x_01]
    U_data.x_05 = [i/u_inlet for i in u_data.x_05]
    U_data.x_09 = [i/u_inlet for i in u_data.x_09]
    U_data.y_01 = [i/H for i in u_data.y_01]
    U_data.y_05 = [i/H for i in u_data.y_05]
    U_data.y_09 = [i/H for i in u_data.y_09]
    U_x_list = [i/u_inlet for i in u_x_list]
    ylist_scaled = [i/H for i in ylist]

    # Geschwindigkeit plotten
    mpl.figure(num=1, dpi=500)
    mpl.plot(U_data.x_01, U_data.y_01, 'b--', label='x/H=1')
    mpl.plot(U_data.x_05, U_data.y_05, 'r--', label='x/H=5')
    mpl.plot(U_data.x_09, U_data.y_09, 'm--', label='x/H=9')
    mpl.plot(U_x_list, ylist_scaled, 'g-', label='Analytical Solution')


    # Achsenbeschriftung
    mpl.xlabel('$U/U_{inlet}, [-]$')
    mpl.ylabel('y/H, [-]')
    # Legende aktivieren
    mpl.legend()
    # Abspeichern als PNG
    mpl.tight_layout()
    mpl.savefig(foldertosave+'Comparison_laminar.png',format="png")

def main():
    """
    this is the function used to call all functions necessary for the task
    """

    data_path = './'
    iterations = getIterations()

    data = readUresults(data_path, iterations)
    plotData(data,data_path)

###############################################################################
if __name__ == "__main__":
    main()