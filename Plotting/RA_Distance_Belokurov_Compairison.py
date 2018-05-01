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

SgrMu = [191.3, 197.5, 194.0, 188.3, 163.8, 157.3, 151.7]
SgrR  = [29.9, 36.7, 36.4, 34.1, 22.3, 23.3, 21.1]

BifMu = [189.1, 204.8, 208.3, 204.7, 188.6, 163.7, 163.2]
BifR  = [45.6, 44.7, 37.1, 36.8, 38.7, 50.0, 48.2]

VirMu = [184.8, 209.7, 195.9, 181.8, 206.9]
VirR = [14.6, 7.1, 13.0, 15.5, 6.1]

wedge = [13, 14, 15, 16, 17, 18, 19]

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
#    tmpra, tmpdec = ac.GCToEq(VirMu[i], 0.0, wedge[i])
#    VirRA.append(tmpra)
#    VirDec.append(tmpdec)
#    VirMag.append(dist_mag(VirR[i]))


plt.figure(1)
plt.plot(SgrRA, SgrMag, "o", label="Leading")

plt.plot(BifRA, BifMag, "o", label="Trailing")
#plt.plot(VirRA, VirMag, "o", label="Vir")

plt.plot(BelRA, BelMag, "o", label="Bel Sgr")
plt.plot(BelCRA, BelCMag, "o", label="Bel C")
plt.legend()
plt.xlim(220, 120)
plt.ylim(19,22)
plt.xlabel("RA")
plt.ylabel("i Magnitude")
for i in range(len(wedge)):
    plt.text(SgrRA[i], SgrMag[i], str(wedge[i]))
    plt.text(BifRA[i], BifMag[i], str(wedge[i]))
#    plt.text(VirRA[i], VirMag[i], str(wedge[i]))
plt.figure(2)
plt.plot(SgrRA, SgrDec, "o", ms=10.0, label="Leading")
plt.plot(BifRA, BifDec, "o",  ms=10.0, label="Trailing")
#plt.plot(VirRA, VirDec, "o", label="Vir")
plt.legend()

for i in range(len(wedge)):
    plt.text(SgrRA[i], SgrDec[i], str(wedge[i]), color="white")
    plt.text(BifRA[i], BifDec[i],  str(wedge[i]), color="white")
#    plt.text(VirRA[i], VirDec[i], str(wedge[i]), color="white")

stars = [ [], [] ]
for i in range(9, 23):
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
