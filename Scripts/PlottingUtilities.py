#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
import numpy as np
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac
import scipy.stats as st
import scipy as sc
from copy import deepcopy
import MSTODensity as MSTO


def flipUD(H):
    for i in range(len(H)/2):
        temp = deepcopy(H[i])
        H[i] = deepcopy(H[len(H) - 1 - i])
        H[len(H) - 1 - i] = deepcopy(temp)
    return H

def CreateMask(input_array):
    H = deepcopy(input_array)
    for i in range(len(input_array)):
        for j in range(len(input_array[i])):
            if input_array[i][j] > 0.0:
                H[i][j] = False
            else:
                H[i][j] = True
                
    return H
    
def DoKDE(RAData, DecData, extent, bins):
    # Peform the kernel density estimate
    xx, yy = np.mgrid[extent[0][0]:extent[0][1]:bins[0], extent[1][0]:extent[1][1]:bins[1]]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([np.array(RAData), np.array(DecData)])
    kernel = st.gaussian_kde(values, bw_method=0.10)
    return np.multiply(np.reshape(kernel(positions).T, xx.shape), float(len(RAData)))
    

def plotKernelDensityDifference(RAData, DecData, RAData2, DecData2, extent, bins):

    f = DoKDE(RAData, DecData, extent, bins)
    f2 = DoKDE(RAData2, DecData2, extent, bins)
    #plt.contour(xx, yy, f, cmap='Blues')
    plt.imshow(np.rot90(f-f2), cmap='Blues', extent=[extent[0][0], extent[0][1], extent[1][0], extent[1][1]], vmin=0, vmax=65)
    return

def plotKernelDensity(RAData, DecData, extent, bins):

    # Peform the kernel density estimate
    f = DoKDE(RAData, DecData, extent, bins)

    #plt.contour(xx, yy, f, cmap='Blues')
    plt.imshow(np.rot90(f), cmap='Blues', extent=[extent[0][0], extent[0][1], extent[1][0], extent[1][1]])
    return

def removeDuplicates(x, threshold = (0.001, 0.001, 0.001)):
    for i in range(len(x[0])):
        for j in range(i+1, len(x[0])):
            if abs(x[0][i] - x[0][j]) < threshold[0] and abs(x[1][i] - x[1][j]) < threshold[1] and abs(x[2][i] - x[2][j]) < threshold[2]:
                del x[0][j]
                del x[1][j]
                del x[2][j]
    return x

def checkGlobularClusters():
    clusters = [ [], [], [], [] ]
    
    f = open("/home/weissj3/Desktop/HarrisCatalog.txt", 'r')
    #File Format 46-51 and 53-58
    
    for line in f:
        if line[46:51] != "     " and  line[53:58] != "     " and line[60:64] != "    ":
            templ, tempb, tempr = float(line[46:51]), float(line[53:58]), float(line[60:64])
            
            tempra, tempdec = ac.lbToEq(templ, tempb)
            
            
            if tempra > 130 and tempra < 250 and tempdec < 35 and tempdec > -5:
                clusters[0].append(tempra)
                clusters[1].append(tempdec)
                clusters[2].append(dist_mag(tempr))
                print line[1:9], templ, tempb, tempr, tempra, tempdec
                
        
    return clusters


        
    
    
def readStarFile_RA(x):
    f = open(x, 'r');
    stars2 = np.array([ map(float, ln.split(', ')) for ln in f ])
    #print len(stars2), len(stars2[0])
    #stars3 = ac.lbToEq(stars2[:,0], stars2[:,1])
    #return stars3[0].tolist(), stars3[1].tolist(), stars2[:,2].tolist()
    return stars2[:,0].tolist(), stars2[:,1].tolist(), stars2[:,2].tolist()

def readStarFile_lb(x):
    f = open(x, 'r');
    f.readline()
    stars2 = np.array([ map(float, ln.replace(',', '').split()) for ln in f ])
    stars3 = ac.lbToEq(stars2[:,0], stars2[:,1])
    return stars3[0].tolist(), stars3[1].tolist(), stars2[:,2].tolist()
    #return stars2[:,0].tolist(), stars2[:,1].tolist(), stars2[:,2].tolist()

def dist_mag(x):
  return ma.log10(x * 100.0) * 5.0 + 3.12
  
def mag_dist(x):
  return round(10.0**((float(x) - 3.12)/5.0)/100., 1) 

