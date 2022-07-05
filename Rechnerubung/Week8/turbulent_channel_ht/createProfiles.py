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

def getIterations(logFile):
    with open(logFile,'r') as fout:
        text = fout.read()
        iterations = re.findall('Time = (.*)', text)[-2]
    return iterations

def readUresults(foldername, iterations):
    """
    This function reads the output file of a simulation
    """
    # Datenobjekt definieren
    data = simData()
    data.u_x = []
    data.u_y = []
    data.t_x = []
    data.t_y = []



    with open(foldername+'postProcessing/sample/'+iterations+'/x_by_H_01_U.xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variablen abspeichern (1. und 2. Spalte)
            data.u_x.append(float(split_line[0]))
            data.u_y.append(float(split_line[1]))

    with open(foldername+'postProcessing/sample/'+iterations+'/x_by_H_01_T.xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variablen abspeichern (1. und 2. Spalte)
            data.t_x.append(float(split_line[0]))
            data.t_y.append(float(split_line[1]))
    # TKE einlesen
    # Datenobjekt zurückgeben
    return data

def plotData(data_x, data_y, foldertosave, filename, label):
    """
    This function plots the data given data object
    """

    # Geschwindigkeit plotten
    mpl.figure(num=1, dpi=500)
    mpl.plot(data_x, data_y, 'r-', label=label)


    # Achsenbeschriftung
    # mpl.xlabel('U_X, $[ms^{-1}]$')
    # mpl.ylabel('y, [m]')
    # Legende aktivieren
    mpl.legend()
    # Abspeichern als PNG
    mpl.tight_layout()
    mpl.savefig(foldertosave+filename,format="png")

def main():
    """
    this is the function used to call all functions necessary for the task
    """

    data_path = './'
    logFile = './log'
    iterations = getIterations(logFile)

    filename_u = 'u_mean.png'
    filename_t = 't_mean.png'

    data = readUresults(data_path, iterations)
    plotData(data.u_x, data.u_y,data_path,filename_u, 'U_X')
    plotData(data.t_x, data.t_y,data_path,filename_t, 'T')

###############################################################################
if __name__ == "__main__":
    main()
