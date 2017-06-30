import sys
sys.path.insert(0, '../Newby-tools/utilities')
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac
import operator
import numpy as np

#Following code borrowed from Helio and Galactrix    
#Requires Isochrones from http://stev.oapd.inaf.it/cgi-bin/cmd
def trunc(f, n):
    f = round(f, n)
    slen = len('%.*f' % (n, f))
    return str(f)[:slen] 
  
def Get_name_iso(age,metal):
    iso_base_name = 'iso_galactrix' 
    metal_iso_name = trunc(metal,2)
    age_iso_name = trunc(age,1)
    age_iso_name   = float(age_iso_name)
    metal_iso_name = float(metal_iso_name)
    if metal_iso_name < -2.1:
        metal_iso_name = -2.1
    if metal_iso_name > 0.3:
        metal_iso_name = 0.3
    if age_iso_name == 0.0:
        age_iso_name =  0.1
    if metal_iso_name >= -0.01:
        metal_iso_name = abs(metal_iso_name)
        metal_iso_name = str(metal_iso_name)
    metal_iso_name = str(metal_iso_name)
    return('../../Isochrones/'+ iso_base_name+'_mh{0}_t{1}e9.dat'.format(metal_iso_name, age_iso_name))
#                             Get_name_iso } 

#My Code

def getAbsGMagnitude(metallicity, colorRange, minMag):
    #Assuming Age doesn't matter so pick small number like 2

    iso_name = Get_name_iso(2.0,metallicity)
    data_iso = np.loadtxt(iso_name)
    #Find all points within color range and through out giant stars
    relevantData = []    
    for i in data_iso:
        color = i[9] - i[10] #g minus r color
        g_mag = i[9]
        if color > colorRange[0] and color < colorRange[1] and g_mag > minMag:
            relevantData.append(i)
    
    if len(relevantData) == 0:
        print "Missing stars within color bounds in Isochrone with metallicity %f" % metallicity
        print "Finding nearest points to color bounds"
        minDistMaxColor = 10000.
        minDistMinColor = 10000.
        indexMaxColor = 0
        indexMinColor = 0
        for i in range(len(data_iso)):
            color = data_iso[i][9] - data_iso[i][10] #g minus r color
            g_mag = data_iso[i][9]
            if g_mag > minMag:        
                if abs(color - colorRange[0]) < minDistMinColor:
                    minDistMinColor = abs(color - colorRange[0])
                    indexMinColor = i
                if abs(color - colorRange[1]) < minDistMinColor:
                    minDistMaxColor = abs(color - colorRange[1])
                    indexMaxColor = i
        relevantData.append(data_iso[indexMinColor])
        relevantData.append(data_iso[indexMaxColor])
        print "(Min, Max) found at (%f, %f)" % (data_iso[indexMinColor][9] - data_iso[indexMinColor][10], data_iso[indexMaxColor][9] - data_iso[indexMaxColor][10]) 
                
    #Average Magnitudes
    average = 0.0
    for i in relevantData:
        average += i[9]
    average = average / float(len(relevantData))
    return average



def getPosition(bounds, value, bins):
    return int((value - bounds[0]) / (bounds[1] - bounds[0]) * (bins))


def CutL(L_low, L_high, stars):
    tempStars = []    
    for i in range(len(stars)):
        tempStars.append([])

    for i in range(len(stars[0])):
        if float(stars[12][i]) <= L_high and float(stars[12][i]) >= L_low and float(stars[21][i]) > -9999.:
            for j in range(len(tempStars)):
                tempStars[j].append(stars[j][i])
    return tempStars

def averageMetallicities(stars, x_bounds, y_bounds, bins):
    averages = []
    N = []
    for i in range(bins[1]):
        averages.append([])
        N.append([])
        for j in range(bins[0]):
            averages[i].append(0.0)
            N[i].append(0.0)
    for i in range(len(stars[0])):
        x = getPosition(x_bounds, float(stars[2][i]), bins[0])
        y = bins[1] - 1 - getPosition(y_bounds, float(stars[13][i]), bins[1])
        averages[y][x] += float(stars[21][i])
        N[y][x] += 1.0

    for i in range(len(averages)):    
        for j in range(len(averages[i])):
            if N[i][j]:
                averages[i][j] = averages[i][j] / N[i][j]
            else:
                averages[i][j] = float('nan')
    return averages


if __name__ == "__main__":
    lbCuts = [[48.5, 52.], [68.5, 71.5], [92.5, 95.5], [108.5, 111.5], [128.5, 131.5], [148.5, 151.5], [176.5, 179.5], [185.5, 188.5], [201.5, 204.5], [227.5, 230.5]]
    file = sys.argv[1]
    for j in range(len(lbCuts)):
        f = open(file,"r")

        cols = f.readline().split(",")
        values = []
        for i in cols:
            values.append([])

        for line in f:
            ln = line.split(",")
            for i in range(len(ln)):
                values[i].append(ln[i])
        
        values = CutL(lbCuts[j][0], lbCuts[j][1], values)
        
        dist = []
        delList = []
        for i in range(len(values[0])):
            absMag = getAbsGMagnitude(float(values[21][i]), [.6, .7], 4.0)
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

        print min(values[2]), max(values[2]), min(values[13]), max(values[13])
        plt.subplot(5,2,j)
        #plt.plot(map(float, values[12]), map(float, values[13]), 'o')
        plt.scatter(map(float, values[2]), map(float, values[13]), c=map(float, values[21]), edgecolor='gray')
        plt.imshow(averageMetallicities(values, [0., 4.5], [-30., 30.], [30, 30]), extent=[0., 4.5,-30, 30], interpolation='none', aspect='auto')    
        plt.xlabel("$Distance (kpc)$")
        plt.ylabel("B")
        plt.title("Metallicity at B and Distance (l between %.1f and %.1f)" % (lbCuts[j][0], lbCuts[j][1]))
        plt.colorbar()
    plt.show()
