#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys
import pylab as lab
import re
import math

fig = plt.figure(1, figsize=(25,20), frameon=False)
sp  = 1
f = open(sys.argv[1], 'r')
params = f.readline()
params = map(float,params.split(", "))
error = f.readline()
error = map(float,error.split(", "))
fit = f.readline()
fit = map(float,fit.split(", "))
paramMin = f.readline()
paramMin = map(float,paramMin.split(", "))
paramMax = f.readline()
paramMax = map(float,paramMax.split(", "))

titles = f.readline()
titles = titles.split(", ")
saveFile = sys.argv[2]

count = 0
for i in range(len(params)):
    ax = plt.subplot(5, 4, sp)

    plt.title(titles[i], y=0.75, fontsize=30)
    ax.errorbar(params[i], 0.0, xerr=error[i], elinewidth=5, capsize=10, capthick=4)
    ax.plot(params[i], 0,'ob', ms=15)
    ax.plot(fit[i], 0,'or', ms=15)
    plt.ylim([-0.1, 0.1])
    plt.xlim([paramMin[i], paramMax[i]])
    ax.get_yaxis().set_visible(False)
    sp += 1
    count += 1
    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['bottom'].set_position('center')
    ax.spines['bottom'].set_linewidth(3)

    # Eliminate upper and right axes
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(labelsize=15)

plt.savefig(saveFile)
