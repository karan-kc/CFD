import numpy as np
import matplotlib.pyplot as plt

import lib as lb

path2sim = "/home/alex/temp/UE12/sim/"

nx = 256
ny = 193
nz = 128

Lx = 8
Ly = 2
Lz = 4

# read y-distribution
filename = path2sim + "yp.dat"
y = np.loadtxt(filename)

x = np.linspace(0, Lx, nx, endpoint=False)
z = np.linspace(0, Lz, nz, endpoint=False)

###############################################################
path2data = path2sim + "data/"
idfld = 1

u = lb.read_snapshot(path2data, "ux", 1, [nx,ny,nz])
v = lb.read_snapshot(path2data, "uy", 1, [nx,ny,nz])
w = lb.read_snapshot(path2data, "uz", 1, [nx,ny,nz])

phi = lb.read_snapshot(path2data, "phi1", 1, [nx,ny,nz])

###############################################################
plt.figure()
plt.pcolormesh(z,y,u[0,:,:], shading="gouraud")
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("z")
plt.ylabel("y")
plt.show()

plt.figure()
plt.pcolormesh(x,y,u[:,:,0].T, shading="gouraud")
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
