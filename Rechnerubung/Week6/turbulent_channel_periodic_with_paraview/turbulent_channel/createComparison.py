#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat June 11 15:15:00 2022

@author: Karan Chodankar
"""

import matplotlib.pyplot as mpl
import math
import numpy as np
import re


class simData(object):
    pass

# def getIterations():
#     with open('./log','r') as fout:
#         text = fout.read()
#         result = re.search('SIMPLE solution converged in (.*) iterations', text)
#     return result.group(1)

def readresults(foldername):
    """
    This function reads the output file of a simulation
    """
    # Datenobjekt definieren
    data = simData()
    data.u_DNS = []
    data.y_DNS = []
    data.u_RANS = []
    data.y_RANS = []


    with open(foldername+'Re950.prof') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()[27:]

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('   ')
            # die benötigten Daten in die Variablen abspeichern (1. und 2. Spalte)
            data.u_DNS.append(float(split_line[3]))
            data.y_DNS.append(float(split_line[2]))
    #TKE einlesen
    with open(foldername+'y+_and_u+') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variable abspeichern (2. Spalte)
            data.y_RANS.append(float(split_line[0]))
            data.u_RANS.append(float(split_line[1]))
    # Reynolds-Spannungen einlesen
    # Datenobjekt zurückgeben
    return data

# def u_x(y, u_inlet, H):
#     h = H #0.2
#     u_max = (3/2)*u_inlet #1.85
#     return u_max*(((4*y)/h)-((4*(y**2))/(h**2)))


def plotData(data, foldertosave):
    """
    This function plots the data given data object
    """

    # Geschwindigkeit plotten
    mpl.figure(num=1, dpi=500)
    mpl.plot(data.y_DNS, data.u_DNS, 'c-', label='DNS')
    mpl.plot(data.y_RANS, data.u_RANS, 'C1-', label='RANS')
    



    # Achsenbeschriftung
    mpl.xlabel('$y^+, [-]$')
    mpl.ylabel('$u^+, [-]$') # 'r' vor dem Text inkludiert backslash, sonst wird die Zeile falsch interpretiert, siehe https://docs.python.org/2/reference/lexical_analysis.html#string-literals
    # Legende aktivieren
    mpl.legend()
    # Abspeichern als PNG
    mpl.tight_layout()
    mpl.savefig(foldertosave+'Comparison_DNS.png',format="png")

def main():
    """
    this is the function used to call all functions necessary for the task
    """

    data_path = './'
    # iterations = getIterations()

    data = readresults(data_path)
    plotData(data,data_path)

###############################################################################
if __name__ == "__main__":
    main()
