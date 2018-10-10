#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
import numpy as np
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac
import copy
from matplotlib.ticker import FuncFormatter, MaxNLocator

outputFile = "PrimaryStars_Redone.txt"
    
    
def readStarFile(x, wedge):
    f = open(x, 'r');
    numStars = int(f.readline())
    stars = np.array([ map(float, ln.split(" ")) for ln in f ])

    stars2 = ac.lbToEq(stars[:,0], stars[:,1])
    starsGC = ac.lb2GC(stars[:,0], stars[:,1], wedge+1)
    mask = np.where(starsGC[1] < -1.25)
    return stars2[0][mask].tolist(), stars2[1][mask].tolist(), stars[:,2][mask].tolist()

#BICMask = [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
BICMask = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
f = open(outputFile, "w")
f.close()
stars1 = [ [], [], [] ]

for i in range(10, 24):
    print "Checking File: %d" % i
#    temp1, temp2, temp3 = readStarFile("/home/weissj3/Desktop/ResimSky_2/SeparatedComponents/Streams_%d.txt" % i, i)
#    temp1, temp2, temp3 = readStarFile("/home/weissj3/Desktop/Newby-tools2/milkyway-tools/milkyway_starfiles/stars-%d.txt" % i, i)
    if BICMask[i-10]:
        temp1, temp2, temp3 = readStarFile("/home/weissj3/Desktop/Newby-tools2/milkyway-tools/milkyway_starfiles/stars-%d.txt" % i, i)
        #temp1, temp2, temp3 = readStarFile("/home/weissj3/Desktop/ResimSky_2/4sSeparatedComponents/BG%d.txt" % i, i)
    else:
        temp1, temp2, temp3 = readStarFile("/home/weissj3/Desktop/ResimSky_2/SeparatedComponents/BG%d.txt" % i, i)
    stars1[0] += temp1
    stars1[1] += temp2
    stars1[2] += temp3


print len(stars1[0])
f = open(outputFile, "a")
for i in range(len(stars1[0])):
    f.write("%f, %f, %f\n" % (stars1[0][i], stars1[1][i], stars1[2][i]))    
    
f.close()


    
