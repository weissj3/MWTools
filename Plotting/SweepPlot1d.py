#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys
import pylab as lab
import re
import math

#Command Line Args
fig = plt.figure(1, figsize=(30,20), frameon=False)
#fig.subplots_adjust(hspace=0.01, wspace=0.01)

sp  = 1
f = open(sys.argv[1], 'r')
params = f.readline()
params = params.split(", ")
saveFile = sys.argv[2]

count = 0
for inputFile in sys.argv[3:]:
    ax = plt.subplot(4, 5, sp)
    f = open(inputFile,'r');
    x = [] 
    y = [] 
    likelihood = []
    
    bestX = 0
    bestY = -999
    for line in f:
        ln = line.split();
        if float(ln[2]) > bestY:
            bestY = float(ln[2])
            bestX = float(ln[0])
        x.append(float(ln[0]))
        y.append(float(ln[2]))

    correctx = [params[count], params[count]]
    correcty = y[0]
    if y[0] > y[len(y)-1]:
        correcty = y[len(y)-1]
    correcty = [correcty, bestY]
    plt.title((inputFile.replace('/', '')).split(".")[2], fontsize=24)
    ax.plot(x,y,'-')
    ax.plot(bestX,bestY,'o')
    ax.plot(correctx, correcty,'-', lw=1.5)
    sp += 1
    count += 1

#plt.show()
plt.savefig(saveFile)
