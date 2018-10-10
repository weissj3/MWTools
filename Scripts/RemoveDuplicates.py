#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
import numpy as np
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac
import copy
from matplotlib.ticker import FuncFormatter, MaxNLocator

def removeDuplicates(stars1, stars2, threshold = (0.1, 0.1, 0.1)):
    f = open("PrimaryStars.txt", "a")
    for i in np.arange(len(stars1[0])):
        out = 1
        for j in np.arange(len(stars2[0])):
            if abs(stars1[0][i] - stars2[0][j]) < threshold[0] and abs(stars1[1][i] - stars2[1][j]) < threshold[1] and abs(stars1[2][i] - stars2[2][j]) < threshold[2]:
                out = 0
                break
        if out:
            f.write("%f, %f, %f\n" % (stars1[0][i], stars1[1][i], stars1[2][i]))
            
    f.close()
    return
    
    
    
def readStarFile(x):
    f = open(x, 'r');
    numStars = int(f.readline())
    stars = np.array([ map(float, ln.split()) for ln in f ])

    stars2 = ac.lbToEq(stars[:,0], stars[:,1])
    return stars2[0].tolist(), stars2[1].tolist(), stars[:,2].tolist()


f = open("PrimaryStars.txt", "w")
f.close()
stars1 = [ [], [], [] ]
stars2 = [ [], [], [] ]
temp1, temp2, temp3 = readStarFile("/home/weissj3/Desktop/Newby-tools2/milkyway-tools/milkyway_starfiles/stars-%d.txt" % 9)
stars2[0] = temp1
stars2[1] = temp2
stars2[2] = temp3

for i in range(10, 24):
    stars1 = copy.deepcopy(stars2)
    temp1, temp2, temp3 = readStarFile("/home/weissj3/Desktop/Newby-tools2/milkyway-tools/milkyway_starfiles/stars-%d.txt" % i)
    stars2[0] = temp1
    stars2[1] = temp2
    stars2[2] = temp3
    print "Checking File: %d" % i
    removeDuplicates(stars1, stars2);

print len(stars2)
f = open("PrimaryStars.txt", "a")
for i in range(len(stars2)):
    f.write("%f, %f, %f\n" % (stars2[0][i], stars2[1][i], stars2[2][i]))    
    
f.close()


    
