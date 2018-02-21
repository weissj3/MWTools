#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
sys.path.insert(0, '../Newby-tools/ThreadedTWGWithDisk')
import numpy as np
import math
import matplotlib.pyplot as plt
import astro_coordinates as ac
import distribution_functions as df

l = []
b = []

for i in range(135, 230):
    templ, tempb, tempr = ac.GC2lbr(i, 0, 1, 19)
    if templ < 50:
        templ+=360
    l.append(templ)
    b.append(tempb)

plt.plot(l,b)
plt.show()
