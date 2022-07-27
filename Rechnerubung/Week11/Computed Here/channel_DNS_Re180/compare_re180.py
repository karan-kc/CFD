#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat June 11 15:15:00 2022

@author: Karan Chodankar
"""

import matplotlib.pyplot as mpl

nu = 4.7679e-05
rho = 1
delta = 1
mu = nu*1
delta = 1
tau_wall = 7.3204e-05
u_tau = tau_wall**(1/2)
delta_nu = nu/u_tau

class simData(object):
    pass

def readUrresults(filename):
    """
    This function reads the output file of a simulation
    """
    # Datenobjekt definieren
    data = simData()
    data.y = []
    data.u = []
    data.uv = []
    data.uu = []
    data.vv = []
    data.ww = []


    with open(filename+'/Uf.xy') as fin:
        # Read lines
        data_lines = fin.readlines()

        # Process line by line
        for line in data_lines:
            # If statement to only perform loop on lines not starting with '%'
            if line.startswith('%') == False:
                # Split:
                split_line = line.split()
                # Save the required data in the variables
                data.y.append(float(split_line[0])/delta_nu)
                data.u.append(float(split_line[1])/u_tau)

    with open(filename+'/u.xy') as fin:
        # Read lines
        data_lines = fin.readlines()
        # Process line by line
        for line in data_lines:
            # If statement to only perform loop on lines not starting with '%'
            if line.startswith('%') == False:
                # Split:
                split_line = line.split()
                # Save the required data in the variables
                data.uu.append(float(split_line[1])/u_tau)

    with open(filename+'/v.xy') as fin:
        # Read lines
        data_lines = fin.readlines()

    # Process line by line
        for line in data_lines:
            # If statement to only perform loop on lines not starting with '%'
            if line.startswith('%') == False:
                 # Split:
                split_line = line.split()
                # Save the required data in the variables
                data.vv.append(float(split_line[1])/u_tau)

    with open(filename+'/w.xy') as fin:
        # Read lines
        data_lines = fin.readlines()

    # Process line by line
        for line in data_lines:
            # If statement to only perform loop on lines not starting with '%'
            if line.startswith('%') == False:
                # Split:
                split_line = line.split()
                # Save the required data in the variables
                data.ww.append(float(split_line[1])/u_tau)
    with open(filename+'/uv.xy') as fin:
        # Read lines
        data_lines = fin.readlines()

        # Process line by line
        for line in data_lines:
            # If statement to only perform loop on lines not starting with '%'
            if line.startswith('%') == False:
                # Split:
                split_line = line.split()
                # Save the required data in the variables
                data.uv.append(float(split_line[1])/(u_tau**2))
    # Datenobjekt zurückgeben
    return data

def readTheirresults(filename):
    """
    This function reads the output file of a simulation
    """
    # Datenobjekt definieren
    jimenez_data = simData()
    jimenez_data.y = []
    jimenez_data.u = []
    jimenez_data.uv = []
    jimenez_data.uu = []
    jimenez_data.vv = []
    jimenez_data.ww = []


    with open(filename) as fin:
        # Read lines
        data_lines = fin.readlines()

        # Process line by line
        for line in data_lines:
            # If statement to only perform loop on lines not starting with '%'
            if line.startswith('%') == False:
                # Split:
                split_line = line.split()
                # Save the required data in the variables
                jimenez_data.y.append(float(split_line[1]))
                jimenez_data.u.append(float(split_line[2]))
                jimenez_data.uv.append(float(split_line[10]))
                jimenez_data.uu.append((float(split_line[3])*float(split_line[3]))**(1/2))
                jimenez_data.vv.append((float(split_line[4])*float(split_line[4]))**(1/2))
                jimenez_data.ww.append((float(split_line[5])*float(split_line[5]))**(1/2))
    # Datenobjekt zurückgeben
    return jimenez_data

def plotData(object, attribute1, attribute2, name, ylabel, linelabel, boolean, line, color, logornot):
    """
    This function plots the data given data object
    """

    # Geschwindigkeit plotten
    mpl.figure(num=1, dpi=500)
    mpl.plot(getattr(object, attribute1), getattr(object, attribute2), color+line, label=linelabel)


    # Achsenbeschriftung
    mpl.xlabel('$y^+$')
    mpl.ylabel(ylabel)
    if logornot:
        mpl.xscale('log')
    # Legende aktivieren
    # Abspeichern als PNG
    mpl.tight_layout()
    mpl.legend()
    mpl.title(r'$Re_\tau{}=180$')
    mpl.savefig(name,format="png")

    if boolean:                 # To clear Graph or not
        mpl.figure().clear()
        mpl.close()
        mpl.cla()
        mpl.clf()


def main():
    """
    this is the function used to call all functions necessary for the task
    """

    data_path_jimenez = 'Re180.prof'
    data_path_my_simulation = 'postProcessing/graphs/1000'

    data_jimenez = readTheirresults(data_path_jimenez)
    data_mine = readUrresults(data_path_my_simulation)

    # Plot u_mean.png

        # Jimenez Database
    plotData(data_jimenez, 'y', 'u', 'u_mean.png', '$u^+$', 'Jimenez database',False, '--', 'k', True)

        # My Simulation
    plotData(data_mine, 'y', 'u', 'u_mean.png', '$u^+$', 'My Simulation',True, '-', 'r', True)


    # Plot fluct.png

    # Jimenez Database
    plotData(data_jimenez, 'y', 'uu', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", '', False,'--', 'k', False)
    plotData(data_jimenez, 'y', 'vv', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", "",False,'--', 'k', False)
    plotData(data_jimenez, 'y', 'ww', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", "",False,'--', 'k', False)
    plotData(data_jimenez, 'y', 'uv', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", "",False,'--', 'k', False)

    # My Simulation
    plotData(data_mine, 'y', 'uu', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", r'$\sqrt{\overline{u'+"'"+'u'+"'}}^+$", False,'-', 'b', False)
    plotData(data_mine, 'y', 'vv', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", r'$\sqrt{\overline{v'+"'"+'v'+"'}}^+$",False,'-', 'C1', False)
    plotData(data_mine, 'y', 'ww', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", r'$\sqrt{\overline{w'+"'"+'w'+"'}}^+$",False,'-', 'y', False)
    plotData(data_mine, 'y', 'uv', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", r'$\overline{u'+"'"+'v'+"'}^+$",False,'-', 'C4', False)



###############################################################################
if __name__ == "__main__":
    main()

# Time for the First Execution Step on My Computer = 8.02s
# Time for the First Execution Step on the Cluster = 1.04s
# Speed-Up = 7.71

# The Speed-Up is in the range I expected. My Machine uses 4 cores, while I used
# 40 cores on the cluster. Based on that the Speed-Up should be 10x. However, multi-core
# processing needs extra headroom to manage the operation of simultaneous simulations. As a result,
# the Speed-Up is reduced.
