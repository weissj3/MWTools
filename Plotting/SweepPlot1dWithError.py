#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys
import pylab as lab
import re
import math as ma

def errorCurve(x, mu, a, c):
    x = x-mu
    return - (x * x * a) + c

#Command Line Args
fig = plt.figure(1, figsize=(30,20), frameon=False)
#fig.subplots_adjust(hspace=0.01, wspace=0.01)
sp  = 1
f = open(sys.argv[1], 'r')
params = map(float, f.readline().split(", "))
saveFile = sys.argv[2]
f = open(sys.argv[3], 'r')
errors = [ i for i in map(float, f.readline().split())]
Normerrors = [ (i / 290.0) for i in errors]

print Normerrors

count = 0
for inputFile in sys.argv[4:]:
    ax = plt.subplot(4, 5, sp)
    f = open(inputFile,'r');
    x = [] 
    y = [] 
    errY= []
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
    a = -ma.log(1.0 / (errors[count] * ma.sqrt(6.28))) / ( 2.0 * errors[count]*errors[count])
    
    if a < 0:
        a = -a
        
    c = -2.973179666011419 
    for i in x:
        errY.append( errorCurve(i, correctx[0], a, c) )
    plt.title((inputFile.replace('/', '')).split(".")[2], fontsize=24)
    ax.plot(x,y,'-')
    ax.plot(bestX,bestY,'o')
    ax.plot(correctx, correcty,'-', lw=1.5)
    ax.plot(x,errY, '-')
    sp += 1
    count += 1

#plt.show()
plt.savefig(saveFile)
