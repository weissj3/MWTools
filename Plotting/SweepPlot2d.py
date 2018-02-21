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

best = [0.0, 0.0]

for line in f:
    ln = line.split();
    if xparam != float(ln[0]) and count != 0:
#        print len(temp);
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
    if lmax < float(ln[2]):
        best = [float(ln[0]), float(ln[1])];
        lmax = float(ln[2])
    if lmin > float(ln[2]): lmin = float(ln[2]);
    count += 1;

print count;
print "best: %3f, %3f" % (best[0], best[1])

extent = [ tmin, tmax, pmin, pmax ];
print "%3f %3f %3f %3f" % (tmin, tmax, pmin, pmax);
x = np.array(x).transpose();

#plt.imshow(x, extent=extent, origin='lower', interpolation='spline16', 
plt.imshow(x, extent=extent, origin='lower', interpolation='none', 
vmin=lmin, vmax=lmax, cmap='gray');
plt.colorbar();
plt.contour(x, 10, extent=extent, vmin=lmin, vmax=lmax, cmap='autumn');
plt.xlabel("Theta");
plt.ylabel("Phi");
plt.title("Theta, Phi Parameter Sweep");
plt.xlim([extent[0], extent[1]]);
plt.ylim([extent[2], extent[3]]);
plt.plot(1.85, 3.05, 'o');
#plt.plot(1.5, 3.18, 'o');
plt.plot(best[0], best[1], 'og');
plt.grid();
plt.show();
