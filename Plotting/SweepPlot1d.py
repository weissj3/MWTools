#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import sys
import pylab as lab
import re
import math


def PlotSweep(inputFile, ax, color):
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
    ax.plot(x,y,'-'+color)
    ax.plot(bestX,bestY,'o'+color, ms=10)
    return correctx, correcty

#Command Line Args
fig = plt.figure(1, figsize=(30,20), frameon=False)
#fig.subplots_adjust(hspace=0.01, wspace=0.01)

sp  = 1
f = open(sys.argv[1], 'r')
params = f.readline()
params = params.split(", ")
saveFile = sys.argv[3]
f = open(sys.argv[2], 'r')
fitParams = map(float, f.readline().split(", "))
fitLikelihood = float(f.readline())

count = 0
for inputFile in sys.argv[4:]:
    ax = plt.subplot(4, 6, sp)

    correctx, correcty = PlotSweep(inputFile, ax, "b")
    ax.plot(correctx[0], correcty[1],'db', ms=10)
    correctx, correcty = PlotSweep("../1DSweepStripe19SimBPLFixed_MWResult/"+inputFile.split("/")[len(inputFile.split("/"))-1], ax, "r")
    ax.plot(fitParams[count], fitLikelihood, 'dr', ms=10)
    ax.annotate((inputFile.replace('/', '')).split(".")[1], (0.5, 0.9), xycoords='axes fraction',  va='center', ha='center', fontsize=18)

    
    
    ax.set_ylim(-3.07, -3.02)
    if count ==1: ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    plt.setp(ax.get_xticklabels(), fontsize=13)
    if (not sp % 6 == 1):
        plt.setp(ax.get_yticklabels(), visible=False)
    else:
        plt.setp(ax.get_yticklabels(), fontsize=14)
    plt.setp(ax.get_xticklabels()[0], visible=False)
    plt.setp(ax.get_xticklabels()[len(ax.get_xticklabels())-1], visible=False)
    if count == 5 or count == 6 or count == 18: plt.setp(ax.get_xticklabels()[len(ax.get_xticklabels())-2], visible=False)
    if sp == 2: sp += 4
    sp += 1
    count += 1

plt.subplots_adjust(wspace = 0.1)
#plt.show()
plt.savefig(saveFile, bbox_inches='tight')
