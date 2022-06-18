#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat June 11 15:15:00 2022

@author: Karan Chodankar
"""

import matplotlib.pyplot as mpl
import math
import re

class simData(object):
    pass

def getIterations(logFile):
    with open(logFile,'r') as fout:
        text = fout.read()
        iterations = re.findall('Time = (.*)', text)[-2]

    return iterations

def get_Tau(shearStressFile):
    notLine = ''
    for notLine in open(shearStressFile,'r'):
        li=notLine.strip()
        if not li.startswith("#"):
            line = notLine.rstrip()
            temp1 = line.split("(")[1]
            temp2 = float(temp1.split(' ')[0])
            return abs(temp2)

def readresults(DNS, RANS, iterations, tau):
    """
    This function reads the output file of a simulation
    """
    # Datenobjekt definieren
    data = simData()
    data.u_DNS = []
    data.y_DNS = []
    data.u_RANS = []
    data.y_RANS = []

    u_tau = math.sqrt(tau)
    nu = 1e-5
    del_nu = nu/u_tau


    with open(DNS) as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()[27:]

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('   ')
            # die benötigten Daten in die Variablen abspeichern (1. und 2. Spalte)
            data.y_DNS.append(float(split_line[2]))
            data.u_DNS.append(float(split_line[3]))
    #TKE einlesen
    with open(RANS) as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variable abspeichern (2. Spalte)
            data.y_RANS.append(float(split_line[0])/del_nu)
            data.u_RANS.append(float(split_line[1])/u_tau)
    # Reynolds-Spannungen einlesen
    # Datenobjekt zurückgeben
    return data


def plotData(data, foldertosave, iterations):
    """
    This function plots the data given data object
    """

    # Geschwindigkeit plotten
    mpl.figure(num=1, dpi=500)
    mpl.plot(data.y_DNS, data.u_DNS, 'c-', label='DNS')
    mpl.plot(data.y_RANS, data.u_RANS, 'C1-', label='RANS')

    # Achsenbeschriftung
    mpl.xlabel('$y^+, [-]$')
    mpl.ylabel('$u^+, [-]$')
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
    shearStressFile = './postProcessing/wallShearStress/0/wallShearStress.dat'
    logFile = './log'
    dns_file = './Re950.prof'
    iterations = getIterations(logFile)
    tau = get_Tau(shearStressFile)
    rans_file = 'postProcessing/sample/'+iterations+'/x_U.xy'

    data = readresults(dns_file, rans_file, iterations, tau)
    plotData(data,data_path,iterations)

###############################################################################
if __name__ == "__main__":
    main()
