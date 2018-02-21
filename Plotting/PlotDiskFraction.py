#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
sys.path.insert(0, '../Newby-tools/ThreadedTWGWithDisk')
import numpy as np
import astro_coordinates as ac
import matplotlib.pyplot as plt
import math as ma
import pylab as lab
import os
from os.path import isfile, join



def thinDisk(z, r):
    return ma.exp(-r/2.250 - abs(z)/.250)

def thickDisk(z, r):
    return ma.exp(-r/3.50 - abs(z)/.700)

def spheroid(z, q, r):
    return 1.0 / (1.0 + ((r * r) + (z/q) * (z/q)) ** (1.75))


ThinDiskWeight = .91875 / .08 * thickDisk(0.0, 8.5) / thinDisk(0.0,8.5)
BackgroundWeight = .00125 / .99875 * (thickDisk(0.0,8.5) + ThinDiskWeight * thinDisk(0.0, 8.5))/spheroid(0.0, 0.8, 8.5)

R = []
ThinDisk = []
ThickDisk = []
Spheroid = []
for i in range(100):
    R.append(float(i) / 10.0);
    x,y,z = ac.GC2xyz(135., 0.0, float(i)/10.0, 19)
    r = ma.sqrt(x * x + y * y)
    tmpThin = ThinDiskWeight * thinDisk(z, r)
    tmpThick = thickDisk(z, r)
    tmpSpher = BackgroundWeight * spheroid(z, 0.8, r)
    total = tmpThin + tmpThick + tmpSpher
    ThinDisk.append(tmpThin / total)
    ThickDisk.append(tmpThick / total)
    Spheroid.append(tmpSpher / total)

plt.plot(R, ThinDisk, label="Thin Disk ($\mu=135$)", lw=1.5)
plt.plot(R, ThickDisk, label="Thick Disk ($\mu=135$)", lw=1.5)
plt.plot(R, Spheroid, label="Spheroid ($\mu=135$)", lw=1.5)

R = []
ThinDisk = []
ThickDisk = []
Spheroid = []
for i in range(100):
    R.append(float(i) / 10.0);
    x,y,z = ac.GC2xyz(230., 0.0, float(i)/10.0, 19)
    r = ma.sqrt(x * x + y * y)
    tmpThin = ThinDiskWeight * thinDisk(z, r)
    tmpThick = thickDisk(z, r)
    tmpSpher = BackgroundWeight * spheroid(z, 0.8, r)
    total = tmpThin + tmpThick + tmpSpher
    ThinDisk.append(tmpThin / total)
    ThickDisk.append(tmpThick / total)
    Spheroid.append(tmpSpher / total)

plt.plot(R, ThinDisk, "--", label="Thin Disk ($\mu=230$)", lw=1.5)
plt.plot(R, ThickDisk, "--", label="Thick Disk ($\mu=230$)", lw=1.5)
plt.plot(R, Spheroid, "--", label="Spheroid ($\mu=230$)", lw=1.5)
plt.axvspan(0., 2.3, alpha=0.3, color='grey')

plt.xlabel("Heliocentric R (kpc)", fontsize=14)
plt.ylabel("Stellar Fraction", fontsize=14)
plt.xticks(fontsize=14)    # fontsize of the tick labels
plt.yticks(fontsize=14)   # fontsize of the tick labels
plt.title("Star Fraction vs Height Above The Disk", fontsize=18)
plt.legend(bbox_to_anchor=(1.0, 0.66), fontsize=10)
plt.show()

