#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
import matplotlib.pyplot as plt
import astro_coordinates as ac
import math as ma

[206.9, 6.05, 0.50, 3.01]

x0,y0,z0 = ac.GC2xyz(206.9, 0.0, 6.05, 19)
x1,y1,z1 = ac.stream2xyz(0.0,0.0,333.0,206.9,6.05,0.50,3.01,19)

#Virgo
x = x1-x0
y = y1-y0
z = z1-z0
print "VIRGO:"
print (x, y, z)
print (ma.sqrt(x*x + y*y + z*z))
print ac.GC2lbr(206.9, 0.0, 6.05, 19)

print ac.xyz2lbr(x0,y0,z0,8.5)
print ac.xyz2lbr(x1,y1,z1,8.5)

#BS
x0,y0,z0 = ac.GC2xyz(163.2, 0.0, 48.2, 19)
x1,y1,z1 = ac.stream2xyz(0.0,0.0,3.0,163.2,48.2,1.36,3.41,19)

x = x1-x0
y = y1-y0
z = z1-z0
print "BS:"
print (x, y, z)
print (ma.sqrt(x*x + y*y + z*z))
print ac.GC2lbr(163.2, 0.0, 48.2, 19)

print ac.xyz2lbr(x0,y0,z0,8.5)
print ac.xyz2lbr(x1,y1,z1,8.5)

