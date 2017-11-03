#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys
import pylab as lab
import re
import math

#Command Line Args
fig = plt.figure(1, figsize=(20,15), frameon=False)
#fig.subplots_adjust(hspace=0.01, wspace=0.01)

sp  = 1

for inputFile in sys.argv[1:]:
    ax = plt.subplot(4, 5, sp)
    f = open(inputFile,'r');
    
    x = [] 
    y = [] 
    likelihood = []
    

    for line in f:
        ln = line.split();
        x.append(float(ln[0]))
        y.append(float(ln[2]))
    saveFile = (inputFile.replace('/', '')).split(".")[1] + ".png"
    plt.title((inputFile.replace('/', '')).split(".")[1])
    ax.plot(x,y,'-')
    sp += 1

plt.show()
#plt.savefig(saveFile)
