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
    
    stars = ac.lbToEq(stars[:,0], stars[:,1])
    return stars[0].tolist(), stars[1].tolist()



def dist_mag(x):
  return ma.log10(x * 100.0) * 5.0 + 3.12

SgrMu = [218.1, 192.8, 186.5, 169.2, 145.2, 190.5, 195.2, 167.1, 192.6, 191.0, 211.3, 163.0, 133.0, 195.8, 195.6]
SgrR  = [41.7,  14.8,  15.0,  13.9,  65.4,  13.9,  41.7,  52.4,  36.4,  46.1,  5.5,   18.9,  17.6,  10.8,  40.6]

BifMu = [235.0, 165.0, 151.2, 235.0, 175.4, 199.6, 185.5, 188.4, 173.0, 174.6, 151.8, 133.0, 209.3, 171.1, 190.0]
BifR  = [4.0,   33.6,  99.8,  4.0,   5.5,   39.4,  14.4,  12.4,  18.5,  42.2,  21.1,  70.4,  37.0,  46.5,  14.6]

VirMu = [208.3, 214.3, 206.8, 235.0, 209.2, 156.5, 192.6, 189.1, 181.0, 174.1, 147.8, 249.0, 184.4, 131.1, 133.0]
VirR =  [15.1,  44.6,  40.0,  55.6,  51.2,  16.5,  35.6,  35.0,  91.5,  21.4,  67.3,  100.0, 15.5,  13.4,  14.2]

wedge = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

BelRA = [215, 210, 205, 200, 195, 190, 185, 180, 175, 170, 165]
BelMag = [21.45, 21.4, 21.35, 21.2, 21.1, 20.9, 20.8, 20.65, 20.4, 20.25, 20.2]

BelCRA = [190, 185, 180]
BelCMag = [21.4, 21.35, 21.45]


SgrRA = []
SgrDec = []
SgrMag = []

BifRA = []
BifDec = []
BifMag = []

VirRA = []
VirDec = []
VirMag = []

for i in range(len(SgrMu)):
    tmpra, tmpdec = ac.GCToEq(SgrMu[i], 0.0, wedge[i])
    SgrRA.append(tmpra)
    SgrDec.append(tmpdec)
    SgrMag.append(dist_mag(SgrR[i]))
    tmpra, tmpdec = ac.GCToEq(BifMu[i], 0.0, wedge[i])
    BifRA.append(tmpra)
    BifDec.append(tmpdec)
    BifMag.append(dist_mag(BifR[i]))
    tmpra, tmpdec = ac.GCToEq(VirMu[i], 0.0, wedge[i])
    VirRA.append(tmpra)
    VirDec.append(tmpdec)
    VirMag.append(dist_mag(VirR[i]))


plt.figure(1)
plt.plot(SgrRA, SgrMag, "bo", label="MW@home")

plt.plot(BifRA, BifMag, "bo", label="MW@home")
plt.plot(VirRA, VirMag, "bo", label="MW@home")

plt.plot(BelRA, BelMag, "r*", label="Bel Sgr")
plt.plot(BelCRA, BelCMag, "g*", label="Bel C")
plt.legend()
plt.xlim(260, 120)
#plt.ylim(19,22)
plt.xlabel("RA")
plt.ylabel("i Magnitude")
for i in range(len(wedge)):
    plt.text(SgrRA[i], SgrMag[i], str(wedge[i])+".1")
    plt.text(BifRA[i], BifMag[i], str(wedge[i])+".2")
    plt.text(VirRA[i], VirMag[i], str(wedge[i])+".3")
plt.figure(2)
plt.plot(SgrRA, SgrDec, "bo", ms=10.0, label="Leading")
plt.plot(BifRA, BifDec, "bo", ms=10.0, label="Trailing")
plt.plot(VirRA, VirDec, "bo", ms=10.0, label="Vir")
#plt.legend()

for i in range(len(wedge)):
    plt.text(SgrRA[i], SgrDec[i], str(wedge[i])+".1", color="white")
    plt.text(BifRA[i], BifDec[i],  str(wedge[i])+".2", color="white")
    plt.text(VirRA[i], VirDec[i], str(wedge[i])+".3", color="white")

stars = [ [], [] ]
for i in range(9, 24):
    temp1, temp2 = readStarFile("/home/weissj3/Desktop/Newby-tools2/milkyway-tools/milkyway_starfiles/stars-%d.txt" % i)
    stars[0] = stars[0] + temp1
    stars[1] = stars[1] + temp2

print len(stars[0]), len(stars[1])
plt.hist2d(stars[0], stars[1], bins=[375, 105], cmap="gray")
plt.colorbar()
plt.xlabel("RA", fontsize=18)
plt.ylabel("Dec", fontsize=18)
plt.xticks(fontsize=16)    # fontsize of the tick labels
plt.yticks(fontsize=16)   # fontsize of the tick labels
plt.xlim(251, 127)
plt.show()
