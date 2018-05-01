#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
import matplotlib.pyplot as plt
import astro_coordinates as ac
import math as ma

[206.9, 6.05, 0.50, 3.01]
deg = 180./ma.pi

x0,y0,z0 = ac.GC2xyz(206.9, 0.0, 6.05, 19)
dx0,dy0,dz0 = ac.stream2xyz(0.0,0.0,1.0,206.9,6.05,0.50*deg,3.01*deg,19)

x1 = -5.48
y1 = -6.18
z1 = 11.26
dx1 = -0.45
dy1 = -0.70
dz1 = -0.56
#Virgo
dx = dx0-x0 
dy = dy0-y0 
dz = dz0-z0 

ax = plt.subplot(2,2,1)
arrows = []
arrows.append(ax.arrow(x0, y0, dx, dy, head_width=1., label="MW@home Fit"))
arrows.append(ax.arrow(x1, y1, dx1, dy1, head_width=1., facecolor="r", label="Newberg et al. (2007)"))
ax.set_ylim([-15, 15])
ax.set_xlim([-15, 15])
ax.set_xlabel("X (kpc)")
ax.set_ylabel("Y (kpc)")
ax.legend(arrows, ["MW@home Fit", "Newberg et al. (2007)"])

ax = plt.subplot(2,2,2)

ax.arrow(x0, z0, dx, dz, head_width=1. )
ax.arrow(x1, z1, dx1, dz1, head_width=1., facecolor="r")
ax.set_ylim([-15, 15])
ax.set_xlim([-15, 15])
ax.set_xlabel("X (kpc)")
ax.set_ylabel("Z (kpc)")

ax = plt.subplot(2,2,3)

ax.arrow(y0, z0, dy, dz, head_width=1. )
ax.arrow(y1, z1, dy1, dz1, head_width=1., facecolor="r")
ax.set_ylim([-15, 15])
ax.set_xlim([-15, 15])
ax.set_xlabel("Y (kpc)")
ax.set_ylabel("Z (kpc)")


#BS
x0,y0,z0 = ac.GC2xyz(163.2, 0.0, 48.2, 19)
x1,y1,z1 = ac.stream2xyz(0.0,0.0,1.0,163.2,48.2,1.36*deg,3.41*deg,19)

#ax = plt.subplot(2,2,1)
#
#ax.arrow(x0, y0, x1, y1, label="Bifurcated Stream")
#
#ax = plt.subplot(2,2,2)

#ax.arrow(x0, z0, x1, z1, label="Bifurcated Stream")

#ax = plt.subplot(2,2,3)

#ax.arrow(y0, z0, y1, z1, label="Bifurcated Stream")
#ax.legend()
plt.show()
