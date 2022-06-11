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
    u_data.x_005 = []
    u_data.y_005 = []
    u_data.x_02 = []
    u_data.y_02 = []
    u_data.x_10 = []
    u_data.y_10 = []


    with open(foldername+'postProcessing/sample/'+iterations+'/x_by_H_005_U.xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variablen abspeichern (1. und 2. Spalte)
            u_data.x_005.append(float(split_line[1]))
            u_data.y_005.append(float(split_line[0]))
    # TKE einlesen
    with open(foldername+'postProcessing/sample/'+iterations+'/x_by_H_02_U.xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variable abspeichern (2. Spalte)
            u_data.x_02.append(float(split_line[1]))
            u_data.y_02.append(float(split_line[0]))
    # Reynolds-Spannungen einlesen
    with open(foldername+'postProcessing/sample/'+iterations+'/x_by_H_10_U.xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variable abspeichern (3. Spalte)
            u_data.x_10.append(float(split_line[1]))
            u_data.y_10.append(float(split_line[0]))
    # Datenobjekt zurückgeben
    return u_data

def u_x(y, u_inlet, H):
    h = H #0.002
    u_max = (3/2)*u_inlet #0.25
    return u_max*(((4*y)/h)-((4*(y**2))/(h**2)))


def plotData(u_data, foldertosave):
    """
    This function plots the data given data object
    """

    ylist = np.linspace(0,0.002,num=1000)
    u_x_list = u_x(ylist, 0.25, 0.002)

    # Geschwindigkeit plotten
    mpl.figure(num=1, dpi=500)
    mpl.plot(u_data.x_005, u_data.y_005, 'b--', label='x/H=0.5')
    mpl.plot(u_data.x_02, u_data.y_02, 'r--', label='x/H=2')
    mpl.plot(u_data.x_10, u_data.y_10, 'm--', label='x/H=10')
    mpl.plot(u_x_list, ylist, 'g-', label='Analytical Solution')




    # Achsenbeschriftung
    mpl.xlabel('$U/U_{inlet}, [-]$')
    mpl.ylabel('y/h, [-]') # 'r' vor dem Text inkludiert backslash, sonst wird die Zeile falsch interpretiert, siehe https://docs.python.org/2/reference/lexical_analysis.html#string-literals
    # Legende aktivieren
    mpl.legend()
    # Abspeichern als PNG
    mpl.tight_layout()
    mpl.savefig(foldertosave+'Comparison.png',format="png")

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
