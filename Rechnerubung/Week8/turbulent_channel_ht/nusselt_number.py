#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat June 11 15:15:00 2022

@author: Karan Chodankar
"""
import numpy as np
import re

H = 0.2
t_u = 343
t_l = 293
rho = 1.225
u_bulk = 1.3452
del_T_w = t_u-t_l
q_T_w = 1.269321e+02
q_theta_w = q_T_w/del_T_w
delta = 0.1
c_p = 1005
mu = 1.831e-5
pr = 0.705
kappa = (c_p*mu)/pr

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
    data.u_y = []
    data.theta_y = []

    with open(foldername+'postProcessing/sample/'+iterations+'/x_by_H_01_U.xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variablen abspeichern (1. und 2. Spalte)
            data.u_y.append(float(split_line[1]))

    with open(foldername+'postProcessing/sample/'+iterations+'/x_by_H_01_T.xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            #Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variablen abspeichern (1. und 2. Spalte)
            data.theta_y.append((float(split_line[1])-t_l)/del_T_w)
    # TKE einlesen
    # Datenobjekt zurückgeben
    return data

def main():
    """
    this is the function used to call all functions necessary for the task
    """
    data_path = './'
    logFile = './log'
    iterations = getIterations(logFile)

    data = readUresults(data_path, iterations)
    u_mean = np.mean(np.array(data.u_y))
    theta_mean = np.mean(np.array(data.theta_y))

    del_theta_l = (1/(u_bulk*delta))*u_mean*theta_mean*(H/2-0)
    nusselt_l = ((2*H)/del_theta_l)*(q_theta_w/kappa)

    re_dh = (2*H*rho*u_bulk)/mu
    nusselt_kays = 0.021*(pr**0.5)*(re_dh**0.8)


    dev = (nusselt_l-nusselt_kays)/nusselt_kays # The Deviation is about 0.5251645338427997%

    print("The deviation from the Kays-Correlation is "+str(dev*100)+"%")



###############################################################################
if __name__ == "__main__":
    main()