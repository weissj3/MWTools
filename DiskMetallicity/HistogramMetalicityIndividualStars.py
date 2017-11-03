import sys
sys.path.insert(0, '../Newby-tools/utilities')
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac
import operator
import MetalicityUtilities as met
import numpy as np
from scipy.integrate import quad

PI = 3.14159265359
SQ2PI = ma.sqrt(2.0 * PI)

def modfit_probability(x, sigma_l = .5, sigma_r = .2):
    sigma = 0.0
    if x < 0.0:
        sigma = sigma_l
    else:
        sigma = sigma_r
    return ma.exp(-(x * x) / (2.0 * sigma * sigma) ) / (.5 * (sigma_r + sigma_l) * SQ2PI)

def lbrtoGalCyl(l,b,r):
    x,y,z = ac.lbr2xyz(l,b,r)
    return ma.sqrt(x*x + y*y)#, z

if __name__ == "__main__":
    lbCuts = [[48.5, 52.], [68.5, 71.5], [92.5, 95.5], [108.5, 111.5], [128.5, 131.5], [148.5, 151.5], [176.5, 179.5], [185.5, 188.5], [201.5, 204.5], [227.5, 230.5]]
    file = sys.argv[1]
    f = open(file,"r")

    cols = f.readline().split(",")
    values = []
    for i in cols:
        values.append([])


    for j in range(len(lbCuts)):
        f = open(file,"r")

        cols = f.readline().split(",")
        tmpvalues = []
        for i in cols:
            tmpvalues.append([])

        for line in f:
            ln = line.split(",")
            for i in range(len(ln)):
                tmpvalues[i].append(ln[i])
        
        tmpvalues = met.CutL(lbCuts[j][0], lbCuts[j][1], tmpvalues)
        for i in range(len(tmpvalues)):
            values[i] = values[i] + tmpvalues[i]
        
    dist = []
    delList = []
    for i in range(len(values[0])):
        absMag = met.getAbsGMagnitude(float(values[21][i]), [.6, .7], 4.0)
        temp_r = ac.getr(float(values[2][i]) - float(values[8][i]), absMag)  
        dist.append(temp_r)
        values[2][i] = temp_r
        if float(values[21][i]) < -2.1:
            print temp_r, values[13][i], float(values[21][i])
        if temp_r > 4.5:
            delList.insert(0,i)
    for i in delList:
        for k in values:
            del k[i]

    weights = [ 1.0 / float(len(values[21])) for i in range(len(values[21])) ]
    plt.hist(map(float, values[21]), bins=35, normed=True, range=[-4.5, .5])
    x = np.linspace(-4.5, 1.0, 100)
    prob = []
    for i in x:
        prob.append(modfit_probability(i + 0.5, .5, .3))
    
    plt.plot(x, prob)

    plt.xlabel("Metalicity")
    plt.ylabel("Counts")
    plt.title("Metalicity Histogram")
    plt.show()
