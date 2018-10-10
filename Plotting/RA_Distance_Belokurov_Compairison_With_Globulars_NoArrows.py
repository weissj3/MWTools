#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
import numpy as np
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac
from matplotlib.ticker import FuncFormatter, MaxNLocator

Primary = int(sys.argv[2])


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
                clusters[3].append(line[1:9])
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

SgrMu = [[], []]
SgrR  = [[], []]
SgrT  = [[], []]
SgrP  = [[], []]
SgrW  = [[], []] 

BifMu = [[], []]
BifR  = [[], []]
BifT  = [[], []]
BifP  = [[], []]
BifW  = [[], []] 

VirMu = [[], []]
VirR  = [[], []]
VirT  = [[], []]
VirP  = [[], []]
VirW  = [[], []] 

f = open(sys.argv[1], 'r')
count = 0
wedge = 9
for line in f:
    if count == 0:
        count +=1
        wedge +=1
        continue
    if count == 4:
        count = 0
        continue
    Bad = 0
    if line[0] == '*':
        Bad = 1
        line = line[1:]
    ln = line.split()
    if count == 1:
        SgrMu[Bad].append(float(ln[1]))
        SgrR[Bad].append(float(ln[2]))
        SgrT[Bad].append(float(ln[3]))
        SgrP[Bad].append(float(ln[4]))
        SgrW[Bad].append(wedge)
    if count == 2:
        BifMu[Bad].append(float(ln[1]))
        BifR[Bad].append(float(ln[2]))
        BifT[Bad].append(float(ln[3]))
        BifP[Bad].append(float(ln[4]))
        BifW[Bad].append(wedge)
    if count == 3:
        VirMu[Bad].append(float(ln[1]))
        VirR[Bad].append(float(ln[2]))
        VirT[Bad].append(float(ln[3]))
        VirP[Bad].append(float(ln[4]))
        VirW[Bad].append(wedge)

    count += 1

wedge = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

BelRA = [215, 210, 205, 200, 195, 190, 185, 180, 175, 170, 165]
BelMag = [21.45, 21.4, 21.35, 21.2, 21.1, 20.9, 20.8, 20.65, 20.4, 20.25, 20.2]

BelCRA = [190, 185, 180]
BelCMag = [21.4, 21.35, 21.45]

clusters = checkGlobularClusters()

SgrRA = [[], []]
SgrDec = [[], []]
SgrMag = [[], []]
SgrArrowRA = [[], []]
SgrArrowDec = [[], []]
SgrArrowMag = [[], []]
SgrNorm = [[], []]

BifRA = [[], []]
BifDec = [[], []]
BifMag = [[], []]
BifArrowRA = [[], []]
BifArrowDec = [[], []]
BifArrowMag = [[], []]
BifNorm = [[], []]

VirRA = [[], []]
VirDec = [[], []]
VirMag = [[], []]
VirArrowRA = [[], []]
VirArrowDec = [[], []]
VirArrowMag = [[], []]
VirNorm = [[], []]

for j in range(len(SgrMu)):
    for i in range(len(SgrMu[j])):
        tmpra, tmpdec = ac.GCToEq(SgrMu[j][i], 0.0, SgrW[j][i])
        SgrRA[j].append(tmpra)
        SgrDec[j].append(tmpdec)
        SgrMag[j].append(dist_mag(SgrR[j][i]))
        tmpra, tmpdec, tmpr = ac.streamToEqR(0.0,0.0,1.0,SgrMu[j][i], SgrR[j][i], SgrT[j][i]*ac.deg, SgrP[j][i]*ac.deg, SgrW[j][i])
        SgrArrowRA[j].append(tmpra[0] - SgrRA[j][i])
        SgrArrowDec[j].append(tmpdec  - SgrDec[j][i])
        SgrArrowMag[j].append(dist_mag(tmpr) - SgrMag[j][i])
        SgrNorm[j].append(ma.sqrt(SgrArrowRA[j][i]**2. + SgrArrowDec[j][i]**2. + SgrArrowMag[j][i]**2.))
for j in range(len(BifMu)):
    for i in range(len(BifMu[j])):       
        tmpra, tmpdec = ac.GCToEq(BifMu[j][i], 0.0, BifW[j][i])
        BifRA[j].append(tmpra)
        BifDec[j].append(tmpdec)
        BifMag[j].append(dist_mag(BifR[j][i]))
        tmpra, tmpdec, tmpr = ac.streamToEqR(0.0,0.0,1.0,BifMu[j][i], BifR[j][i], BifT[j][i]*ac.deg, BifP[j][i]*ac.deg, BifW[j][i])
        BifArrowRA[j].append(tmpra[0] - BifRA[j][i])
        BifArrowDec[j].append(tmpdec - BifDec[j][i])
        BifArrowMag[j].append(dist_mag(tmpr) - BifMag[j][i])
        BifNorm[j].append(ma.sqrt(BifArrowRA[j][i]**2. + BifArrowDec[j][i]**2. + BifArrowMag[j][i]**2.))
for j in range(len(VirMu)):
    for i in range(len(VirMu[j])):        
        tmpra, tmpdec = ac.GCToEq(VirMu[j][i], 0.0, VirW[j][i])
        VirRA[j].append(tmpra)
        VirDec[j].append(tmpdec)
        VirMag[j].append(dist_mag(VirR[j][i]))
        tmpra, tmpdec, tmpr = ac.streamToEqR(0.0,0.0,1.0,VirMu[j][i], VirR[j][i], VirT[j][i]*ac.deg, VirP[j][i]*ac.deg, VirW[j][i])
        VirArrowRA[j].append(tmpra[0] - VirRA[j][i])
        VirArrowDec[j].append(tmpdec - VirDec[j][i])
        VirArrowMag[j].append(dist_mag(tmpr) - VirMag[j][i])
        VirNorm[j].append(ma.sqrt(VirArrowRA[j][i]**2. + VirArrowDec[j][i]**2. + VirArrowMag[j][i]**2.))


plt.figure(1)

plt.plot(SgrRA[0], SgrMag[0], "bo", ms=10.0, label="MW@home")

plt.plot(BifRA[0], BifMag[0], "bo", ms=10.0)
plt.plot(VirRA[0], VirMag[0], "bo", ms=10.0)

#plt.plot(SgrRA[1], SgrMag[1], "ro", label="MW@home Bad")

#plt.plot(BifRA[1], BifMag[1], "ro", label="MW@home Bad")
#plt.plot(VirRA[1], VirMag[1], "ro", label="MW@home Bad")
plt.plot(clusters[0], clusters[2], "gd", ms=10, label="Clusters")

#for j in range(len(SgrRA)):
#    for i in range(len(SgrRA[j])):
#        plt.arrow(SgrRA[j][i], SgrMag[j][i], SgrArrowRA[j][i]/SgrNorm[j][i], SgrArrowMag[j][i]/SgrNorm[j][i], #length_includes_head=True, head_width=.1, head_length=.4)
#for j in range(len(BifRA)):
#    for i in range(len(BifRA[j])):
#        plt.arrow(BifRA[j][i], BifMag[j][i], BifArrowRA[j][i]/BifNorm[j][i], BifArrowMag[j][i]/BifNorm[j][i], #length_includes_head=True, head_width=.1, head_length=.4)
#for j in range(len(VirRA)):
#    for i in range(len(VirRA[j])):
#        plt.arrow(VirRA[j][i], VirMag[j][i], VirArrowRA[j][i]/VirNorm[j][i], VirArrowMag[j][i]/VirNorm[j][i], #length_includes_head=True, head_width=.1, head_length=.4)

plt.plot(BelRA, BelMag, "r*", ms=10.0, label="Bel Sgr")
plt.plot(BelCRA, BelCMag, "g*", ms=10.0, label="Bel C")
plt.legend(loc=4)
plt.xlim(260, 120)
plt.xlabel("RA", fontsize=18)
plt.ylabel("i Magnitude", fontsize=18)
plt.xticks(fontsize=16)    # fontsize of the tick labels
plt.yticks(fontsize=16) 
ax2 = plt.gca().twinx()
ax2.set_ylabel('Distance (kpc)', fontsize=18)
ax2.set_ylim(16, 24)
ax2.yaxis.set_major_formatter(FuncFormatter(format_fn))
ax2.yaxis.set_tick_params(labelsize=16)

#plt.ylim(19,22)
for j in range(len(SgrRA)):
    for i in range(len(SgrRA[j])):
        plt.text(SgrRA[j][i]-1.0, SgrMag[j][i], str(SgrW[j][i])+".1")
for j in range(len(BifRA)):
    for i in range(len(BifRA[j])):
        plt.text(BifRA[j][i]-1.0, BifMag[j][i], str(BifW[j][i])+".2")
for j in range(len(VirRA)):
    for i in range(len(VirRA[j])):
        plt.text(VirRA[j][i]-1.0, VirMag[j][i], str(VirW[j][i])+".3")
for j in range(len(clusters[0])):
    plt.text(clusters[0][j]-1.0, clusters[2][j], str(clusters[3][j]))
plt.figure(2)
plt.plot(SgrRA[0], SgrDec[0], "bo", ms=10.0, label="Leading")
plt.plot(BifRA[0], BifDec[0], "bo", ms=10.0, label="Trailing")
plt.plot(VirRA[0], VirDec[0], "bo", ms=10.0, label="Vir")
plt.plot(SgrRA[1], SgrDec[1], "ro", ms=10.0, label="Leading_Bad")
plt.plot(BifRA[1], BifDec[1], "ro", ms=10.0, label="Trailing_Bad")
plt.plot(VirRA[1], VirDec[1], "ro", ms=10.0, label="Vir_Bad")
#for j in range(len(SgrRA)):
#    for i in range(len(SgrRA[j])):
#        plt.arrow(SgrRA[j][i], SgrDec[j][i], SgrArrowRA[j][i]/SgrNorm[j][i], SgrArrowDec[j][i]/SgrNorm[j][i], color="white", #length_includes_head=False, head_width=.2, head_length=1.0)
#for j in range(len(BifRA)):
#    for i in range(len(BifRA[j])):
#        plt.arrow(BifRA[j][i], BifDec[j][i], BifArrowRA[j][i]/BifNorm[j][i], BifArrowDec[j][i]/BifNorm[j][i], color="white", #length_includes_head=False, head_width=.2, head_length=1.0)
#for j in range(len(VirRA)):
#    for i in range(len(VirRA[j])):
#        plt.arrow(VirRA[j][i], VirDec[j][i], VirArrowRA[j][i]/VirNorm[j][i], VirArrowDec[j][i]/VirNorm[j][i], color="white", #length_includes_head=False, head_width=.2, head_length=1.0)
#plt.legend()

for j in range(len(SgrRA)):
    for i in range(len(SgrRA[j])):
        plt.text(SgrRA[j][i], SgrDec[j][i], str(SgrW[j][i])+".1", color="white")
for j in range(len(BifRA)):
    for i in range(len(BifRA[j])):
        plt.text(BifRA[j][i], BifDec[j][i],  str(BifW[j][i])+".2", color="white")
for j in range(len(VirRA)):
    for i in range(len(VirRA[j])):
        plt.text(VirRA[j][i], VirDec[j][i], str(VirW[j][i])+".3", color="white")

stars = [ [], [], [] ]
if Primary:
    stars[0], stars[1], stars[2] = readStarFile_RA("/home/weissj3/Desktop/MWTools/Data/PrimaryStars/PrimaryStars_2.txt")
    temp = np.where((np.array(stars[2]) < 20.0) & (np.array(stars[2]) > 10.0))# and (stars[2] > 24.0))
    
    stars[0] = np.array(stars[0])[temp[0]]
    stars[1] = np.array(stars[1])[temp[0]]
    stars[2] = np.array(stars[2])[temp[0]]
    
else:
    for i in range(9, 24):
        temp1, temp2, temp3 = readStarFile_lb("/home/weissj3/Desktop/Newby-tools2/milkyway-tools/milkyway_simulated_north/AllSkyRebuildStars-%d.txt" % i)
        stars[0] = stars[0] + temp1
        stars[1] = stars[1] + temp2
        stars[2] = stars[2] + temp3

#stars = removeDuplicates(stars)
print len(stars[0]), len(stars[1])

plt.hist2d(stars[0], stars[1], bins=[280, 80], range=[[120, 260], [-5, 35]], cmap="binary", vmin=0, vmax=35)
plt.colorbar()
plt.plot(clusters[0], clusters[1], "gd", ms=10, label="Clusters")
plt.xlabel("RA", fontsize=18)
plt.ylabel("Dec", fontsize=18)
plt.xticks(fontsize=16)    # fontsize of the tick labels
plt.yticks(fontsize=16)   # fontsize of the tick labels
plt.xlim(251, 127)
plt.show()
