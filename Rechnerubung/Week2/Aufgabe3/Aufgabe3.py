#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 11:20:51 2022
@author: Alexander Stroh
"""
# Module importieren
import numpy
from math import pi
import matplotlib.pyplot as plt
import rosenhead


def runSimulation(inputnvort):
    # Main Definitions
    U = 1;
    nvort = inputnvort
    lambd = 2 * pi
    ampl = 0.1 * lambd
    dt = 0.05 * lambd / U
    nt = 8

    # Initialisierung der Koordinaten für Wirbelzentren (Vortex Center)
    vortpos_x = numpy.linspace(lambd / nvort, lambd, nvort)
    vortpos_y = ampl * numpy.sin(vortpos_x)
    x = numpy.linspace(lambd / nvort, lambd, nvort)
    y = ampl * numpy.sin(vortpos_x)

    # Initialisierung der induzierten Geschwindigkeiten (Induced Velocity)
    u = numpy.zeros(numpy.size(vortpos_x))
    v = numpy.zeros(numpy.size(vortpos_x))

    # Erstellung der Achsenumgeung mit subplots (Subplots with axis)
    fig, axs = plt.subplots(nt, sharex=True, figsize=(5, 10))
    fig.tight_layout(pad=3.0)

    # y axis =y/lambd, x axis = x/lambd
    # Computes velocity in x and y direction
    # t iterates the subplots from 0 to nt
    for t in range(0, nt):
        # Uses vortpos to calculate and output new u,v values
        u, v = rosenhead.updateVelocity(U, vortpos_x, vortpos_y, lambd, nvort)

        # Updating Position uses velocity to change vortpos (Output vortpos_x,vortpos_y)
        [vortpos_x, vortpos_y] = rosenhead.updatePosition(dt, u, v, vortpos_x, vortpos_y)

        # Plots current vortpos_x,vortpo_y array for given t
        rosenhead.plotVortexSheet(t, axs, U, dt, vortpos_x, vortpos_y, lambd)

    plt.show()  # Added so that the interactive python console respects the order (of printed text)


# Run simulation for 12 nodes
nodes = 12
print("Number of nodes: ", nodes)
runSimulation(nodes)

# Run simulation for 120 nodes
nodes = 120
print("Number of nodes: ", nodes)
runSimulation(nodes)