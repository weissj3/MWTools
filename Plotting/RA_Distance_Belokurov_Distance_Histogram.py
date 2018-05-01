#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
import numpy as np
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac

def readStarFile(x):
    f = open(x, 'r');
    numStars = int(f.readline())
    stars = np.array([ map(float, ln.split()) for ln in f ])

    stars2 = ac.lbToEq(stars[:,0], stars[:,1])
    return stars2[0].tolist(), stars2[1].tolist(), stars[:,2].tolist()

stars = [ [], [], [] ]

for i in range(9, 23):
    temp1, temp2, temp3 = readStarFile("/home/weissj3/Desktop/Newby-tools2/milkyway-tools/milkyway_starfiles/stars-%d.txt" % i)
    stars[0] = stars[0] + temp1
    stars[1] = stars[1] + temp2
    stars[2] = stars[2] + temp3

print len(stars[0]), len(stars[1])
#plt.hist2d(stars[0], stars[1], bins=[375, 105], cmap="gray")
#plt.colorbar()
#plt.xlabel("RA", fontsize=18)
#plt.ylabel("Dec", fontsize=18)
#plt.xticks(fontsize=16)    # fontsize of the tick labels
#plt.yticks(fontsize=16)   # fontsize of the tick labels
#plt.xlim(251, 127)


ra = [ 185 ]
sgr_dec = [ 11.2 ]
bif_dec = [ 20.2 ]

sgr_stars = [ [], [], [] ]
bif_stars = [ [], [], [] ]

for i in range(len(stars[0])):
    for j in range(len(ra)):
        if stars[0][i] < ra[j] + 3 and stars[0][i] > ra[j] - 3:
            if stars[1][i] < sgr_dec[j] + 3 and stars[1][i] > sgr_dec[j] - 3:
                sgr_stars[0].append(stars[0][i])
                sgr_stars[1].append(stars[1][i])
                sgr_stars[2].append(stars[2][i])
                #sgr_stars[2].append(ac.getg(stars[2][i], 3.12))
            if stars[1][i] < bif_dec[j] + 3 and stars[1][i] > bif_dec[j] - 3:
                bif_stars[0].append(stars[0][i])
                bif_stars[1].append(stars[1][i])
                bif_stars[2].append(stars[2][i])
                #bif_stars[2].append(ac.getg(stars[2][i], 3.12))

plt.subplot(1,2,1)
plt.hist(sgr_stars[2], bins=20)
plt.subplot(1,2,2)
plt.hist(bif_stars[2], bins=20)

plt.show()
