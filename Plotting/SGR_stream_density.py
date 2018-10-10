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

Primary = int(sys.argv[1])

stars = [ [], [], [] ]
Simstars = [ [], [], [] ]

def top(x):
    return -2./15. * x + 42.0

def bottom(x):
    return -2./15. * x + 34.67
    
def getArea(low, high):
    a = - 1./15. * high * high + 42.0 * high + 1./15. * low * low + 42.0 * low
    b = - 1./15. * high * high + 34.67 * high + 1./15. * low * low + 34.67 * low
    return a + b
    
if Primary:
    high = 40.0
    low  = 20.0
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



temp = ac.EqTolb(stars[0],stars[1])
stars[0] = temp[0]
stars[1] = temp[1]

lambda_beta_stars = list(ac.lb2sgr(stars[0],stars[1],stars[2]))

starHist = PU.flipUD(np.histogram2d(lambda_beta_stars[3], lambda_beta_stars[4], bins=[220, 40], range=[[200, 310], [-20, 20]])[0].transpose())

plt.figure(1)
plt.imshow(starHist, extent=[200, 310, -20, 20], cmap="binary", vmin=0)
plt.plot(range(200, 310, 1), top(np.array(map(float, range(200, 310, 1)))))
plt.plot(range(200, 310, 1), bottom(np.array(map(float, range(200, 310, 1)))))
plt.colorbar()


temp = np.where((top(np.array(lambda_beta_stars[3])) > lambda_beta_stars[4]) & (bottom(np.array(lambda_beta_stars[3])) < lambda_beta_stars[4]))


lambda_beta_stars[3] = np.array(lambda_beta_stars[3])[temp[0]]
lambda_beta_stars[4] = np.array(lambda_beta_stars[4])[temp[0]]
lambda_beta_stars[5] = np.array(lambda_beta_stars[5])[temp[0]]

starHist = PU.flipUD(np.histogram2d(lambda_beta_stars[3], lambda_beta_stars[4], bins=[110, 1], range=[[200, 310], [0, 15]])[0].transpose())

starHist2 = PU.flipUD(np.histogram2d(lambda_beta_stars[3], lambda_beta_stars[4], bins=[220, 40], range=[[200, 310], [-20, 20]])[0].transpose())

background = MSTO.CreateObservedBackground([int(high), int(low)], "TestSave3_65kpcConvolvedALast.data")
print background.shape

BGSub = np.array([0.0 for i in range(200, 310)])

for i in range(200, 310):
    for j in range(int(bottom(i)), int(top(i))):
        ra, dec, r = ac.sgr2Eq(i, j, 25)
        print int((dec+5.)*2), int((ra-120.)*2)
        BGSub[i-200] += background[int((dec+5.)*2)][int((ra-120.)*2)]


plt.figure(2)
plt.plot(range(200, 310, 1), (starHist[0]-BGSub)/np.array(getArea(np.array(map(float, range(201, 311, 1))), np.array(map(float, range(200, 310, 1))))))
plt.figure(3)
plt.imshow(starHist, extent=[200, 310, 0, 15], cmap="binary", vmin=0)
plt.colorbar()
plt.figure(4)
plt.imshow(starHist2, extent=[200, 310, -20, 20], cmap="binary", vmin=0)
plt.xlabel("Lambda", fontsize=18)
plt.ylabel("Beta", fontsize=18)
plt.colorbar()
plt.show()
