#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat August 1 15:15:00 2022

@author: Karan Chodankar
"""

import matplotlib.pyplot as mpl
import numpy as np
import lib as lb

re_tau = 180
rho = 1
pressure_grad = 0.0018  # Didn't match value from slurm.out, tried a bunch of values
delta = 1
u_tau = (pressure_grad/rho)**(1/2)
delta_nu = delta/re_tau
num_snapshots = 50  # 1-50


class simData(object):
    pass

def readUrresults(pathname):
    """
    This function reads the output file of a simulation
    """
    u_arr = []
    v_arr = []
    w_arr = []
    uv_arr = []
    uu_arr = []
    vv_arr = []
    ww_arr = []
    # phi_arr = []
    # pp_arr = []

    nx = 256
    ny = 193
    nz = 128

    # read y-distribution
    filename_y = pathname + 'yp.dat'
    y = np.loadtxt(filename_y)

    ###############################################################
    data_folder = pathname + 'data/'
    idfld = num_snapshots  # 1-50

    for steps in range(1, idfld+1):

        u = lb.read_snapshot(data_folder, "ux", steps, [nx, ny, nz])
        v = lb.read_snapshot(data_folder, "uy", steps, [nx, ny, nz])
        w = lb.read_snapshot(data_folder, "uz", steps, [nx, ny, nz])
        #phi = lb.read_snapshot(pathname, "phi1", steps, [nx, ny, nz])
        #pp = lb.read_snapshot(pathname, "pp", steps, [nx, ny, nz])

        u_arr.append(u)
        v_arr.append(v)
        w_arr.append(w)
        #phi_arr.append(phi)
        #pp_arr.append(pp)
        if steps == idfld:
            print('\nNow calculating the mean and variance values:')

    u_arr = np.reshape(u_arr, [idfld, nx, ny, nz])
    v_arr = np.reshape(v_arr, [idfld, nx, ny, nz])
    w_arr = np.reshape(w_arr, [idfld, nx, ny, nz])
    #phi_arr = np.reshape(phi_arr, [idfld, nx, ny, nz])
    #pp_arr = np.reshape(pp_arr, [idfld, nx, ny, nz])

    u_mean = []
    v_mean = []
    w_mean = []

    for i in range(len(y)):
        u_meanD = np.mean(u_arr[:, :, i, :])
        v_meanD = np.mean(v_arr[:, :, i, :])
        w_meanD = np.mean(w_arr[:, :, i, :])

        uu_meanD = np.mean(u_arr[:, :, i, :]*u_arr[:, :, i, :])
        vv_meanD = np.mean(v_arr[:, :, i, :]*v_arr[:, :, i, :])
        ww_meanD = np.mean(w_arr[:, :, i, :]*w_arr[:, :, i, :])
        uv_meanD = np.mean(u_arr[:, :, i, :]*v_arr[:, :, i, :])

        u_mean.append(u_meanD)
        v_mean.append(v_meanD)
        w_mean.append(w_meanD)

        uu_arr.append(uu_meanD - u_meanD*u_meanD)
        vv_arr.append(vv_meanD - v_meanD*v_meanD)
        ww_arr.append(ww_meanD - w_meanD*w_meanD)
        uv_arr.append(uv_meanD - u_meanD*v_meanD)

    u_mean = np.array(u_mean)

    uu_arr = np.array(uu_arr)
    vv_arr = np.array(vv_arr)
    ww_arr = np.array(ww_arr)
    uv_arr = np.array(uv_arr)

    u_plus = u_mean/u_tau
    y_plus = y/delta_nu
    uu_plus = np.sqrt(uu_arr)/u_tau
    vv_plus = np.sqrt(vv_arr)/u_tau
    ww_plus = np.sqrt(ww_arr)/u_tau
    uv_plus = uv_arr/u_tau**2

    my_data = simData()
    my_data.y = y_plus.tolist()
    my_data.u = u_plus.tolist()
    my_data.uv = uv_plus.tolist()
    my_data.uu = uu_plus.tolist()
    my_data.vv = vv_plus.tolist()
    my_data.ww = ww_plus.tolist()

    return my_data

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
            if not line.startswith('%'):
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
    mpl.savefig(name, format="png")

    if boolean:                 # To clear Graph or not
        mpl.figure().clear()
        mpl.close()
        mpl.cla()
        mpl.clf()


def main():
    """
    this is the function used to call all functions necessary for the task
    """

    data_path_jimenez = '../Re180.prof'
    data_path_my_simulation = '../simulation/'

    data_jimenez = readTheirresults(data_path_jimenez)
    data_mine = readUrresults(data_path_my_simulation)

    # Plot u_mean.png

        # Jimenez Database
    plotData(data_jimenez, 'y', 'u', 'u_mean.png', '$u^+$', 'Jimenez database', False, '--', 'k', True)

        # My Simulation
    plotData(data_mine, 'y', 'u', 'u_mean.png', '$u^+$', 'My Simulation', True, '-', 'r', True)


    # Plot fluct.png

        # Jimenez Database
    plotData(data_jimenez, 'y', 'uu', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", '', False, '--', 'k', False)
    plotData(data_jimenez, 'y', 'vv', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", "", False, '--', 'k', False)
    plotData(data_jimenez, 'y', 'ww', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", "", False, '--', 'k', False)
    plotData(data_jimenez, 'y', 'uv', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", "", False, '--', 'k', False)

        # My Simulation
    plotData(data_mine, 'y', 'uu', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", r'$\sqrt{\overline{u'+"'"+'u'+"'}}^+$", False, '-', 'b', False)
    plotData(data_mine, 'y', 'vv', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", r'$\sqrt{\overline{v'+"'"+'v'+"'}}^+$", False, '-', 'C1', False)
    plotData(data_mine, 'y', 'ww', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", r'$\sqrt{\overline{w'+"'"+'w'+"'}}^+$", False, '-', 'y', False)
    plotData(data_mine, 'y', 'uv', 'fluct.png', '$v_i$'+"'"+'$v_i$'+"'", r'$\overline{u'+"'"+'v'+"'}^+$", False, '-', 'C4', False)


# Only about 5 snapshots are needed for my simulation values to start closely coinciding with the literature values
# However, the simulation values keep getting closer all the way up to 50 snapshots (The Graphs also gets smoother)
# Did not need to create temporary arrays as I created a 20GB swapfile to deal with the insufficient RAM
###############################################################################
if __name__ == "__main__":
    main()
