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

lmin = 0.0;
lmax = -10.0;
tmin = 5.0;
tmax = 0.0;
pmin = 5.0;
pmax = 0.0;
xparam = 0.0;
count = 0;


for line in f:
    ln = line.split();
    if xparam != float(ln[0]) and count != 0:
        print len(temp);
        x.append(temp);
        temp = [];
        xparam = float(ln[0]);
    if count == 0:
        temp = [];
        xparam = float(ln[0]);
    temp.append(float(ln[2]));
    if tmin > float(ln[0]): tmin = float(ln[0]);
    if tmax < float(ln[0]): tmax = float(ln[0]);
    if pmin > float(ln[1]): pmin = float(ln[1]);
    if pmax < float(ln[1]): pmax = float(ln[1]);
    count += 1;

print count;

extent = [ tmin, tmax, pmin, pmax ];
print "%3f %3f %3f %3f" % (tmin, tmax, pmin, pmax);
x = np.array(x).transpose();

for row in x:
    for i in row:
        if lmin > i: lmin = i;
        if lmax < i: lmax = i; 




plt.imshow(x, extent=extent, origin='lower', interpolation='spline16', vmin=lmin, vmax=lmax, cmap='gray');
plt.colorbar();
plt.contour(x, 5, extent=extent, vmin=lmin, vmax=lmax, cmap='autumn');
plt.xlabel("Theta");
plt.ylabel("Phi");
plt.title("Theta, Phi Parameter Sweep");
plt.xlim([extent[0], extent[1]]);
plt.ylim([extent[2], extent[3]]);
plt.plot(1.5, 3.18, 'o');
plt.grid();
plt.show();
