#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def solveSim (inputNumCells):
    varMu=1
    varPi=1
    h=10
    numCells=inputNumCells

    # Domain Definition
    delta_y=h/numCells
    y=np.linspace(delta_y/2,h-delta_y/2,numCells)
    c=varMu/(delta_y**2)

    # Koeffizientenmatrix
    A=np.zeros([numCells,numCells])

    # Q-Vector
    Q=U=np.zeros([numCells,1])

    # innere Stützstellen
    for i in range(1,numCells-1):
        A[i,i-1]= 1*c
        A[i,i]  = -2*c
        A[i,i+1]= 1*c

        # Q Vector, constant pressure gradient
        Q[i]=-varPi

    # Boundaries
    # Left Rand, Dirichlet BC
    A[0,0] = -3*c
    A[0,1] = 1*c
    Q[0]   = -varPi-2*c*0

    # Right Rand, Dirichlet BC
    A[-1,-1] = -3*c
    A[-1,-2] = 1*c
    Q[-1]   = -varPi-2*c*0

    # Solution
    plt.figure()
    U=(np.linalg.solve(A, Q))
    U=np.concatenate(([[0]],U,[[0]]))
    y=np.concatenate(([0],y,[h]))

    # plot
    plt.plot(y,U,'r-o')

    y2=np.linspace(0,h,100)
    U2=-varPi/(2*varMu)*y2**2+varPi/(2*varMu)*h*y2
    plt.plot(y2,U2,'b-')
    plt.show()

    errorSum1=0
    errorSum2=0
    counter=0

    for val in U:
        analyticalVal=-varPi/(2*varMu)*y[counter]**2+varPi/(2*varMu)*h*y[counter]
        error=val-analyticalVal
        errorSum1=errorSum1+error
        errorSum2=errorSum2+error**2
        counter=counter+1

    #errorSum2=np.sqrt(errorSum2)
    errorSum1=float(errorSum1)
    errorSum2=float(errorSum2)
    print ("Sum of errors: "+str(errorSum1))
    print ("Sum of squared errors: "+str(errorSum2))
    return errorSum1

error1=solveSim(5)
error2=solveSim(10)
error3=solveSim(15)
errorVals=[error1, error2, error3]
nodeVals=[5,10,15]
plt.figure()
plt.plot(nodeVals, errorVals)
plt.show()
p=np.log(errorVals[0]/errorVals[-1])/np.log(nodeVals[-1]/nodeVals[0])
print('p = '+str(p))