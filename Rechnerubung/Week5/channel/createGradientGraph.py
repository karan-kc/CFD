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
    grad_u_data = simData()
    grad_u_data.x_01 = []  # Distance from inlet (at H/2 centerline)
    grad_u_data.y_01 = []  # Velocity Gradient

    with open(foldername+'postProcessing/sample/'+iterations+'/gradient_U_grad(U).xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variablen abspeichern (1. und 2. Spalte)
            grad_u_data.x_01.append(float(split_line[0]))
            grad_u_data.y_01.append(float(split_line[1]))
    # Datenobjekt zurückgeben
    return grad_u_data


def plotData(u_data, foldertosave):
    """
    This function plots the data given data object
    """
    # Geschwindigkeit plotten
    mpl.figure(num=1, dpi=500)
    mpl.plot(u_data.x_01, u_data.y_01, 'C1-', label='grad(U) at H/2')

    # Achsenbeschriftung
    mpl.xlabel('Distance from Inlet, [mm]')
    mpl.ylabel('Velocity Gradient, [1/s]')
    # Legende aktivieren
    mpl.legend()
    # Abspeichern als PNG
    mpl.tight_layout()
    mpl.savefig(foldertosave+'grad(U).png',format="png")

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
