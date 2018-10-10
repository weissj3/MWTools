#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
sys.path.insert(0, '../Scripts')
import numpy as np
import math as ma
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import astro_coordinates as ac
from matplotlib.ticker import FuncFormatter, MaxNLocator
import scipy.stats as st
import scipy as sc
from copy import deepcopy
import MSTODensity as MSTO
import PlottingUtilities as PU

Primary = int(sys.argv[2])

def format_fn(tick_val, tick_pos):
    return PU.mag_dist(tick_val)

SgrMu = [[[], []], [[], []], [[], []], [[], []]]
SgrR  = [[[], []], [[], []], [[], []], [[], []]]
SgrT  = [[[], []], [[], []], [[], []], [[], []]]
SgrP  = [[[], []], [[], []], [[], []], [[], []]]
SgrW  = [[[], []], [[], []], [[], []], [[], []]]

f = open(sys.argv[1], 'r')
count = 0
wedge = 9
for line in f:
    if count == 0:
        count +=1
        wedge +=1
        continue
    if count == 5:
        count = 0
        continue
    Bad = 0
    if line[0] == '*':
        Bad = 1
        line = line[1:]
    ln = line.split()
    if count == 1:
        SgrMu[count-1][Bad].append(float(ln[1]))
        SgrR[count-1][Bad].append(float(ln[2]))
        SgrT[count-1][Bad].append(float(ln[3]))
        SgrP[count-1][Bad].append(float(ln[4]))
        SgrW[count-1][Bad].append(wedge)
    if count == 2:
        SgrMu[count-1][Bad].append(float(ln[1]))
        SgrR[count-1][Bad].append(float(ln[2]))
        SgrT[count-1][Bad].append(float(ln[3]))
        SgrP[count-1][Bad].append(float(ln[4]))
        SgrW[count-1][Bad].append(wedge)
    if count == 3:
        SgrMu[count-1][Bad].append(float(ln[1]))
        SgrR[count-1][Bad].append(float(ln[2]))
        SgrT[count-1][Bad].append(float(ln[3]))
        SgrP[count-1][Bad].append(float(ln[4]))
        SgrW[count-1][Bad].append(wedge)
    if count == 4:
        if len(ln) > 0:
            SgrMu[count-1][Bad].append(float(ln[1]))
            SgrR[count-1][Bad].append(float(ln[2]))
            SgrT[count-1][Bad].append(float(ln[3]))
            SgrP[count-1][Bad].append(float(ln[4]))
            SgrW[count-1][Bad].append(wedge)

    count += 1

wedge = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

BelRA = [215, 210, 205, 200, 195, 190, 185, 180, 175, 170, 165]
BelMag = [21.45, 21.4, 21.35, 21.2, 21.1, 20.9, 20.8, 20.65, 20.4, 20.25, 20.2]

BelCRA = [190, 185, 180]
BelCMag = [21.4, 21.35, 21.45]

clusters = PU.checkGlobularClusters()

SgrRA = [[[], []], [[], []], [[], []], [[], []]]
SgrDec = [[[], []], [[], []], [[], []], [[], []]]
SgrMag = [[[], []], [[], []], [[], []], [[], []]]
SgrArrowRA = [[[], []], [[], []], [[], []], [[], []]]
SgrArrowDec = [[[], []], [[], []], [[], []], [[], []]]
SgrArrowMag = [[[], []], [[], []], [[], []], [[], []]]
SgrNorm = [[[], []], [[], []], [[], []], [[], []]]

for k in range(len(SgrMu)):
    for j in range(len(SgrMu[k])):
        for i in range(len(SgrMu[k][j])):
            tmpra, tmpdec = ac.GCToEq(SgrMu[k][j][i], 0.0, SgrW[k][j][i])
            SgrRA[k][j].append(tmpra)
            SgrDec[k][j].append(tmpdec)
            SgrMag[k][j].append(PU.dist_mag(SgrR[k][j][i]))
            tmpra, tmpdec, tmpr = ac.streamToEqR(0.0,0.0,1.0,SgrMu[k][j][i], SgrR[k][j][i], SgrT[k][j][i]*ac.deg, SgrP[k][j][i]*ac.deg, SgrW[k][j][i])
            SgrArrowRA[k][j].append(tmpra[0] - SgrRA[k][j][i])
            SgrArrowDec[k][j].append(tmpdec  - SgrDec[k][j][i])
            SgrArrowMag[k][j].append(PU.dist_mag(tmpr) - SgrMag[k][j][i])
            SgrNorm[k][j].append(ma.sqrt(SgrArrowRA[k][j][i]**2. + SgrArrowDec[k][j][i]**2. + SgrArrowMag[k][j][i]**2.))

plt.figure(1)

for i in range(len(SgrRA)):
    plt.plot(SgrRA[i][0], SgrMag[i][0], "bo", label="MW@home")
#    plt.plot(SgrRA[i][1], SgrMag[i][1], "ro", label="Bad MW@home")

#plt.plot(SgrRA[1], SgrMag[1], "ro", label="MW@home Bad")

#plt.plot(BifRA[1], BifMag[1], "ro", label="MW@home Bad")
#plt.plot(VirRA[1], VirMag[1], "ro", label="MW@home Bad")
plt.plot(clusters[0], clusters[2], "gd", ms=10, label="Clusters")

#plt.ylim(19,22)
for k in range(len(SgrRA)):
    for j in range(len(SgrRA[k])):
        for i in range(len(SgrRA[k][j])):
            plt.text(SgrRA[k][j][i], SgrMag[k][j][i], str(SgrW[k][j][i])+"."+str(k+1))

for k in range(len(SgrRA)):
    for j in range(len(SgrRA[k])):
        for i in range(len(SgrRA[k][j])):
            plt.arrow(SgrRA[k][j][i], SgrMag[k][j][i], SgrArrowRA[k][j][i]/SgrNorm[k][j][i], SgrArrowMag[k][j][i]/SgrNorm[k][j][i], length_includes_head=True, head_width=.1, head_length=.4)

plt.plot(BelRA, BelMag, "r*", label="Bel Sgr")
plt.plot(BelCRA, BelCMag, "g*", label="Bel C")
plt.legend(loc=4)
plt.xlim(260, 120)
plt.xlabel("RA", fontsize=18)
plt.ylabel("i Magnitude", fontsize=18)
plt.xticks(fontsize=16)    # fontsize of the tick labels
plt.yticks(fontsize=16) 
ax2 = plt.gca().twinx()
ax2.set_ylabel('Distance (kpc)', fontsize=18)
ax2.set_ylim(14, 24)
ax2.yaxis.set_major_locator(MaxNLocator(24))
ax2.yaxis.set_major_formatter(FuncFormatter(format_fn))
ax2.yaxis.set_tick_params(labelsize=16)



plt.figure(2)
for k in range(len(SgrRA)):
    plt.plot(SgrRA[k][0], SgrDec[k][0], "bo", ms=5.0)
    plt.plot(SgrRA[k][1], SgrDec[k][1], "ro", ms=10.0)
    
for k in range(len(SgrRA)):
    for j in range(len(SgrRA[k])):
        for i in range(len(SgrRA[k][j])):
            plt.arrow(SgrRA[k][j][i], SgrDec[k][j][i], SgrArrowRA[k][j][i]/SgrNorm[k][j][i], SgrArrowDec[k][j][i]/SgrNorm[k][j][i], color="white", length_includes_head=False, head_width=.2, head_length=1.0)

for k in range(len(SgrRA)):
    for j in range(len(SgrRA[k])):
        for i in range(len(SgrRA[k][j])):
            plt.text(SgrRA[k][j][i], SgrDec[k][j][i], str(SgrW[k][j][i])+"."+str(k+1), color="white")


stars = [ [], [], [] ]
Simstars = [ [], [], [] ]
if Primary:
    high = 15.0
    low  = 8.0
#    stars[0], stars[1], stars[2] = readStarFile_RA("/home/weissj3/Desktop/MWTools/Scripts/PrimaryStars2.txt")
#    stars[0], stars[1], stars[2] = readStarFile_RA("/home/weissj3/Desktop/MWTools/Scripts/PrimaryStarsAllSky4Stream.txt") 
    stars[0], stars[1], stars[2] = PU.readStarFile_RA("/home/weissj3/Desktop/MWTools/Scripts/PrimaryStars_Redone.txt")
    temp = np.where((np.array(stars[2]) < high) & (np.array(stars[2]) > low))# and (stars[2] > 24.0))
    
    stars[0] = np.array(stars[0])[temp[0]]
    stars[1] = np.array(stars[1])[temp[0]]
    stars[2] = np.array(stars[2])[temp[0]]
    
    Simstars[0], Simstars[1], Simstars[2] = PU.readStarFile_RA("/home/weissj3/Desktop/MWTools/Scripts/PrimaryStarsAllSkySim4StreamBG.txt")
    temp = np.where((np.array(Simstars[2]) < high) & (np.array(Simstars[2]) > low))# and (stars[2] > 24.0))
    
    Simstars[0] = np.array(Simstars[0])[temp[0]]
    Simstars[1] = np.array(Simstars[1])[temp[0]]
    Simstars[2] = np.array(Simstars[2])[temp[0]]
    
else:
    for i in range(10, 24):
        temp1, temp2, temp3 = PU.readStarFile_lb("/home/weissj3/Desktop/Newby-tools2/milkyway-tools/milkyway_simulated_north/AllSkyRebuildStars-%d.txt" % i)
        stars[0] = stars[0] + temp1
        stars[1] = stars[1] + temp2
        stars[2] = stars[2] + temp3

#stars = PU.removeDuplicates(stars)
print len(stars[0]), len(stars[1])
#PU.plotKernelDensity(stars[0], stars[1], extent=[[120, 260], [-5, 35]], bins=[280j, 80j])
#PU.plotKernelDensityDifference(stars[0], stars[1], Simstars[0], Simstars[1], extent=[[120, 260], [-5, 35]], bins=[280j, 80j])
#BGHistogram = PU.flipUD(np.array(MSTO.CreateObservedBackground([int(low), int(high)], "../Scripts/TestSave3_65kpcConvolvedTriaxial_Increased.data")))

BGHistogram = PU.flipUD(np.array(MSTO.CreateObservedBackground([int(low), int(high)], "TestSave3_65kpcConvolvedALast.data")))
#BGHistogram = PU.flipUD(np.array(MSTO.CreateObservedBackground([int(low), int(high)], "TestSave3_65kpc.data")))
starHistogram = PU.flipUD(np.histogram2d(stars[0], stars[1], bins=[280, 80], range=[[120, 260], [-5, 35]])[0].transpose())
stars = np.ma.masked_array(BGHistogram, PU.CreateMask(starHistogram))
#stars2 = np.ma.masked_array(BGHistogram2, PU.CreateMask(starHistogram))
plt.imshow(stars, extent=[120, 260, -5, 35], cmap="binary", vmax=25)
#plt.hist2d(stars[0], stars[1], bins=[280, 80], range=[[120, 260], [-5, 35]], cmap="binary")
#plt.plot(stars[0], stars[1], 'o', ms=0.1) #, bins=[240, 80], range=[[120, 260], [-5, 35]], cmap="binary", vmax=180)
plt.colorbar()
plt.plot(clusters[0], clusters[1], "gd", ms=10, label="Clusters")
plt.xlabel("RA", fontsize=18)
plt.ylabel("Dec", fontsize=18)
plt.xticks(fontsize=16)    # fontsize of the tick labels
plt.yticks(fontsize=16)   # fontsize of the tick labels
plt.xlim(251, 127)
plt.title("%d kpc to %d kpc background" % (low, high))
plt.show()
