#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
import numpy as np
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac
from matplotlib.ticker import FuncFormatter, MaxNLocator

Primary = int(sys.argv[1])


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
    stars2 = np.array([ map(float, ln.replace(',', '').split()) for ln in f ])
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


def format_fn(tick_val, tick_pos):
    return mag_dist(tick_val)



stars = [ [], [], [] ]
if Primary:
       for i in range(10, 24):
        temp1, temp2, temp3 = readStarFile_lb("/home/weissj3/Desktop/Newby-tools2/milkyway-tools/milkyway_starfiles/stars-%d.txt" % i)
        stars[0] = stars[0] + temp1
        stars[1] = stars[1] + temp2
        stars[2] = stars[2] + temp3 
else:
    for i in range(10, 24):
        temp1, temp2, temp3 = readStarFile_lb("/home/weissj3/Desktop/ResimSky_2/AllSkyRebuildStars%d.txt" % i)
        stars[0] = stars[0] + temp1
        stars[1] = stars[1] + temp2
        stars[2] = stars[2] + temp3

#stars = removeDuplicates(stars)
print len(stars[0]), len(stars[1])
plt.hist2d(stars[0], stars[1], bins=[280, 80], range=[[120, 260], [-5, 35]], cmap="binary", vmax=180)
plt.colorbar()
plt.xlabel("RA", fontsize=18)
plt.ylabel("Dec", fontsize=18)
plt.xticks(fontsize=16)    # fontsize of the tick labels
plt.yticks(fontsize=16)   # fontsize of the tick labels
plt.xlim(251, 127)
plt.show()
