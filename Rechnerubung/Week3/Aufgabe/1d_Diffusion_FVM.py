#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:02:28 2020

@author: alex
"""

import numpy as np
import matplotlib.pyplot as plt

# Konstanten
L=10
cells=100
Tw=20
kappa = 1
Ao = 1

# Domain Definition

delta_x=L/cells
x=np.linspace(delta_x/2,L-delta_x/2,cells)

# Koeffizientenmatrix
A=np.zeros([cells,cells])

# Q-Vektor

Q=np.zeros([cells,1])

w=np.zeros([cells,1])
w[int(cells/3):int(2*cells/3)]=1



# innere Stützstellen
for i in range(1,cells-1):
    A[i,i-1]= 1 * (kappa * Ao / delta_x)
    A[i,i]  = -2* (kappa * Ao / delta_x)
    A[i,i+1]= 1 * (kappa * Ao / delta_x)
    
    # Q Vektor
    Q[i]=-w[i]*delta_x * Ao
    
# Randwerte
# linker Rand
A[0,0] = -3 *  (kappa * Ao / delta_x)
A[0,1] = 1  *  (kappa * Ao / delta_x)
Q[0]   = -delta_x *Ao * w[0] - 2*kappa*Ao*Tw/delta_x

# Rechter Rand 
A[-1,-1] = -1 *  (kappa * Ao / delta_x)
A[-1,-2] = 1  *  (kappa * Ao / delta_x)
Q[-1]   = -delta_x *Ao * w[-1]


# Lösung

T=np.linalg.solve(A, Q)

# plotten
plt.plot(x,T,'r-o')
plt.plot(x,w,'b--')

# oder plotten inklsive Randwerte
#plt.plot(np.append(np.append(0,x),L),np.append(np.append(Tw,T),T[-1]),'b-o')

