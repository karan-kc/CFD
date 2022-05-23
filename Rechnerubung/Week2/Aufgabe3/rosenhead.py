# Rosenhead module - a set of functions for reproduction of the Rosenhead simulation

import numpy
from math import pi
import matplotlib.pyplot as plt

def compVelocity(lambd,y1,y,x1,x):
    """
    This function computes induced velocity from acting (x,y) to the considered (x1,y1) vortex

    Parameters
    ----------
    lambd : float
        wavelength
    y1 : float
        y coordinate position of the considered vortex
    y : float
        y coordinate position of the acting vortex
    x1 : float
        x coordinate position of the considered vortex
    x : float
        x coordinate position of the acting vortex

    Returns
    -------
    u,v
        induced velocities from the acting to the considered vortex in 2 directions

    """
    if numpy.cosh(2*pi*(y1-y)/lambd) != numpy.cos(2*pi*(x1-x)/lambd):
        u=numpy.sinh(2*pi*(y1-y)/lambd) / ( numpy.cosh(2*pi*(y1-y)/lambd) - numpy.cos(2*pi*(x1-x)/lambd) )
    else:
        u = 0

    if numpy.cosh(2*pi*(y1-y)/lambd) != numpy.cos(2*pi*(x1-x)/lambd):
        v=numpy.sin(2*pi*(x1-x)/lambd)/(numpy.cosh(2*pi*(y1-y)/lambd)-numpy.cos(2*pi*(x1-x)/lambd))
    else:
        v = 0
    return [u, v]

def updateVelocity(U, vortpos_x, vortpos_y, lambd, nvort):
    """
    The function computes the mutually induced velocity from all the vortices to all the other vortex centers

    Parameters
    ----------
    U : float
        velocity
    vortpos_x : float
        vortex position on x
    vortpos_y : float
        vortex position on y
    lambd : float
        wavelength
    nvort : int
        amount of considered vortices

    Returns
    -------
    u,v
        updated induced velocities for all vortex centers.

    """
    u=numpy.zeros(numpy.size(vortpos_x))
    v=numpy.zeros(numpy.size(vortpos_x))
    for vorttodo in range(0,nvort):
        
        for i in range(0,nvort):
            [utmp,vtmp] = compVelocity(lambd, vortpos_y[vorttodo], vortpos_y[i],vortpos_x[vorttodo], vortpos_x[i])
            u[vorttodo] += utmp
            v[vorttodo] += vtmp
    u=U*u/nvort    
    v=-U*v/nvort
    return [u, v]

def updatePosition(dt,u,v,vortpos_x,vortpos_y):
    """
    The function shifts vortices according to prescribed velocity and time-step

    Parameters
    ----------
    dt : float
        time step
    u : TYPE
        velocity in x
    v : float
        velocity in y
    vortpos_x : float
        vortex position on x
    vortpos_y : float
        vortex position on y

    Returns
    -------
    vortpos_x,vortpos_y
        new vortex positions

    """
    vortpos_x+=u*dt
    vortpos_y+=v*dt
    
    return [vortpos_x,vortpos_y]

def plotVortexSheet(t, axs, U, dt, vortpos_x, vortpos_y, lambd):
    """
    The function plots a distribution of vortex sheet into an axis environment at a certain position

    Parameters
    ----------
    t : int
        position/location in the subplot
    axs : Array of object
        axis environment
    U : float
        velocity
    dt : float
        time step
    vortpos_x : float
        vortex position on x
    vortpos_y : float
        vortex position on y
    lambd : float
        wavelength

    Returns
    -------
    None.

    """
    forplotx=numpy.concatenate((numpy.append(0,vortpos_x/lambd),1+vortpos_x/lambd))
    forploty=numpy.concatenate((numpy.append(0,vortpos_y/lambd),vortpos_y/lambd))
    
    axs[t].plot(forplotx,forploty)

    axs[t].set_ylabel('$y/ \lambda$')
    axs[t].set_xlim([0,2])
    axs[t].set_ylim([-0.3,0.3])
    axs[t].set_title('$t=$'+str((t+1)*dt*U/lambd)+'$\lambda/U$')

