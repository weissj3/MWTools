#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
import numpy as np
import math as ma
import astro_coordinates as ac

def readStarFile(x):
    f = open(x, 'r');
    numStars = int(f.readline())
    stars = np.array([ map(float, ln.split()) for ln in f ])
    
    stars2 = ac.lb2GC(stars[:,0], stars[:,1], 22)
    return stars2[0].tolist(), stars2[1].tolist(), stars[:,2].tolist()
    
temp1, temp2, temp3 = readStarFile("/home/weissj3/Desktop/Newby-tools2/milkyway-tools/milkyway_starfiles/stars-22.txt")

print "Mu " + str(min(temp1)) + " " + str(max(temp1))

print "Nu " + str(min(temp2)) + " " + str(max(temp2))

print "R " + str(min(temp3)) + " " + str(max(temp3))
