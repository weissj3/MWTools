#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys
import pylab as lab
import re
import math

#Command Line Args
input = sys.argv[1];
f = open(input,'r');

x = []; y = []; likelihood = [];


for line in f:
    ln = line.split();
    x.append(float(ln[0]));
    y.append(float(ln[2]));

plt.plot(x,y,'-');
plt.show()
