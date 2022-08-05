#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat June 11 15:15:00 2022

@author: Karan Chodankar
"""
import matplotlib.pyplot as mpl


class simData(object):
    pass


def readandplotresults():
    """
    This function reads the output file of a simulation
    """
    # Datenobjekt definieren
    data = simData()
    data.cd = []
    data.cl = []
    data.tiempo = []

    notLine = ''
    for notLine in open('./postProcessing/forceCoeffs_object/0/forceCoeffs.dat','r'):
        li=notLine.strip()
        if not li.startswith("#"):
            line = notLine.rstrip()
            data.tiempo.append(float(line.split("\t")[0]))
            data.cd.append(float(line.split("\t")[2]))
            data.cl.append(float(line.split("\t")[3]))


    fig, ax1 = mpl.subplots()
    mpl.suptitle('$c_{l}$' + ' and ' + '$c_{d}$' + ' against time')
    ax2 = ax1.twinx()
    a, =  ax1.plot(data.tiempo, data.cl, color='blue', label='$c_{l}$')
    b, = ax2.plot(data.tiempo, data.cd, color='green', label='$c_{d}$')
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p],
               loc= 'lower right', fontsize= 'small')

    ax1.set_xlabel('Time, [s]')
    ax1.set_ylabel('$c_{l}, [-]$')
    ax2.set_ylabel('$c_{d}, [-]$')

    # Abspeichern als PNG
    mpl.tight_layout()
    mpl.savefig('./drag_coefficient_plot.png', format="png", dpi=500)


def main():
    """
    this is the function used to call all functions necessary for the task
    """
    readandplotresults()

if __name__ == "__main__":
    main()
