#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
sys.path.insert(0, '../Newby-tools/ThreadedTWGWithDisk')
import numpy as np
import math
import matplotlib.pyplot as plt
import astro_coordinates as ac
import distribution_functions as df

EpsBG = float(sys.argv[1])
Q = float(sys.argv[2])

#x,y,z = ac.GC2xyz(235., 0.0, 0.0, 19)
#print x,y,z

#total_density = (1.0 - EpsBG) * df.thick_disk_density(x, y, z) + EpsBG * df.hernquist_profile(x, y, z, Q, 12.0)

#disk_fraction = (1.0 - EpsBG) * df.thick_disk_density(x, y, z) / total_density

#hernquist_fraction = EpsBG * df.hernquist_profile(x, y, z, Q, 12.0) / total_density

#print "Disk Fraction: %3f    Hernquist Fraction: %3f    Total Density: %f" % (disk_fraction, hernquist_fraction, total_density)

total_density = []
disk_fraction = []
hernquist_fraction = []
r = []

for i in range(100):
    r.append(float(i)/10.0)
    
    x,y,z = ac.GC2xyz(185., 0.0, float(i)/10.0, 19)

    total_density.append((1.0 - EpsBG) * df.thick_disk_density(x, y, z) + EpsBG * df.hernquist_profile(x, y, z, Q, 12.0))
    
    disk_fraction.append((1.0 - EpsBG) * df.thick_disk_density(x, y, z) / total_density[i])

    hernquist_fraction.append(EpsBG * df.hernquist_profile(x, y, z, Q, 12.0) / total_density[i])
    
plt.plot(r, disk_fraction, label="Disk Fraction ($\mu=135$)", lw=1.5)
plt.plot(r, hernquist_fraction, label="Hernquist Fraction ($\mu=135$)", lw=1.5)

total_density = []
disk_fraction = []
hernquist_fraction = []
r = []

for i in range(100):
    r.append(float(i)/10.0)
    
    x,y,z = ac.GC2xyz(230., 0.0, float(i)/10.0, 19)

    total_density.append((1.0 - EpsBG) * df.thick_disk_density(x, y, z) + EpsBG * df.hernquist_profile(x, y, z, Q, 12.0))
    
    disk_fraction.append((1.0 - EpsBG) * df.thick_disk_density(x, y, z) / total_density[i])

    hernquist_fraction.append(EpsBG * df.hernquist_profile(x, y, z, Q, 12.0) / total_density[i])
    
plt.plot(r, disk_fraction, "--", label="Disk Fraction ($\mu=230$)", lw=1.5)
plt.plot(r, hernquist_fraction, "--", label="Hernquist Fraction ($\mu=230$)", lw=1.5)
plt.legend(bbox_to_anchor=(1.0, 0.66))
plt.title("Thick Disk and Hernquist Fraction Within Wedge", fontsize=18) 
plt.xlabel("Heliocentric R (kpc)", fontsize=14)
plt.ylabel("Stellar Fraction", fontsize=14)
plt.xticks(fontsize=14)    # fontsize of the tick labels
plt.yticks(fontsize=14)   # fontsize of the tick labels
plt.axvspan(0., 2.3, alpha=0.3, color='grey')
plt.show()
