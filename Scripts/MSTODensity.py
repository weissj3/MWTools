#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
import scipy as sc
import numpy as np
import math as ma
import astro_coordinates as ac
import pickle
import matplotlib.pyplot as plt

this = sys.modules[__name__]
global FullSkyModel
SQ2PI = sc.sqrt(2.0 * ma.pi)
offset = 2
center_offset = float(offset) + 0.5

def modfit_error(x, modfit):
    """Detection efficiency Corrected for Modfit"""
    if modfit:
        ay = [5.61945007e2, -1.67343282e1, 1.09325822e-1, 1.34993610e-3, -1.42044161e-5, 0.0, 0.0, 0.0]
        ar = [8.55878159, -1.04891551e1, 3.51630757, -2.29741062e-01, 6.72278105e-03, -1.01910181e-04, 7.82787167e-07, -2.41452056e-09]
        total = (ay[0] + ar[0]) + (ay[1] + ar[1]) * (x) + (ay[2] + ar[2]) * (x * x) + (ay[3] + ar[3]) * (x * x * x) + (ay[4] + ar[4]) * x**4 + (ay[5] + ar[5]) * x**5 + (ay[6] + ar[6]) * x**6 + (ay[7] + ar[7]) * x**7
        if total < 0.0: 
            #print "ERROR Modfit Error = %4f" % (total/532.0)
            total = 0.0;
        return (total/532.0)
    else:
        return 1.0

def sigmoid_error(x, modfit, modulus=None):
    """Application of detection efficiency"""    
    s = [0.9402, 1.6171, 23.5877]
    if modulus != None:
        s[2] = s[2] - modulus
    detection_efficiency = s[0] / (np.exp(s[1]*(x - s[2])) + 1.)
    return detection_efficiency * modfit_error(ac.getr(x), modfit)

def DiskDensity(x,y,z):
    R = sc.sqrt( (x*x) + (y*y) )
    Z = abs(z)
    return ma.exp(Z * (-1.428571429) + R * (-0.285714286)) 
    
def HernquistDensity(x,y,z,q,r0=12.0):
    """ Galactic-centric hernquist density profile """
    r = sc.sqrt( (x*x) + (y*y) + ((z*z)/(q*q)) )
    inv_rho = r*(r + r0)*(r + r0)*(r + r0)
    return (1.0/inv_rho)


def BGDensity(x,y,z,q,A,weight,r0=12.0):
    return ((weight) * HernquistDensity(x,y,z,q) + (1.0 - weight) * DiskDensity(x,y,z)) * A
    
def SausageDensity(x,y,z):
    xp = x * ma.cos(- 0.35) - y * ma.sin(- 0.35)
    yp = x * ma.sin(- 0.35) + y * ma.cos(- 0.35)
    x = xp
    y = yp
    r = (x * x + y * y + z * z)
    req = 12.2
    q = .84 - (.84 - 0.57) * ma.exp(1. - (ma.sqrt(r * r +  req * req)/ req)) # I am not sure about r here.  Check this.
    p = 1.27
    reoverreb = (x * x + y * y / (p*p) + z * z / (q * q))  #I am pretty sure r_eb is just 1
    return ma.pow(reoverreb, -2.96) * ma.pow(1. + reoverreb, -2.96)
    
    
def BGStars(ra,dec,r):
    #Use pyramids to do sketchy integration
    #V1 = .3333333 * r[0] * r[0] * r[0] * abs(ra[1] - ra[0]) * abs(dec[1] - dec[0]) * ac.rad * ac.rad
    #V2 = .3333333 * r[1] * r[1] * r[1] * abs(ra[1] - ra[0]) * abs(dec[1] - dec[0]) * ac.rad * ac.rad
    #V = V2 - V1
    center_ra = (ra[0] + ra[1])/2.0
    center_dec = (dec[0] + dec[1])/2.0
    center_r = (r[0] + r[1])/2.0
    V = r[0] * r[0] * ma.sin((90.0 - center_dec) * ac.rad) * abs(r[1] - r[0]) * abs(ra[1] - ra[0]) * abs(dec[1] - dec[0]) * ac.rad * ac.rad
    l,b = ac.EqTolb(center_ra, center_dec)
    x,y,z = ac.lbr2xyz(l,b,center_r)
    #return V * BGDensity(x,y,z,0.58,300000000,0.9970)
    #return V * BGDensity(x,y,z,0.58,341315437,0.9970)
    return V * SausageDensity(x,y,z)# * 100131543700000.
    
def CreateBackgroundDensity(extent, bins, r):
    Histogram = []
    ra_array = np.linspace(extent[0][0], extent[0][1], bins[0]+1)
    dec_array = np.linspace(extent[1][0], extent[1][1], bins[1]+1)
    r_array= np.linspace(r[0], r[1], 6)
    for i in range(len(dec_array)-1):
        temp = []
        for j in range(len(ra_array)-1):
            temp.append(0.0)
            for k in range(len(r_array)-1):
                ra_integral= np.linspace(ra_array[j],ra_array[j+1], 3)
                dec_integral = np.linspace(dec_array[i],dec_array[i+1], 3)
                for l in range(len(ra_integral)-1):
                    for m in range(len(dec_integral)-1):
                        temp[j] += BGStars([ra_integral[l], ra_integral[l+1]],[dec_integral[m], dec_integral[m+1]],[r_array[k],r_array[k+1]])
        Histogram.append(temp)
    return Histogram

def StarConvolution(g, r, width):
    sigma_l = .36
    sigma_r = ((0.52 / (1.0 + sc.exp(12.0 - r))) + 0.76)
    sigma = .36
    if g > 0:
        sigma = sigma_l
    else:
        sigma = sigma_r
    
    return (sc.exp(-(g*g) / (2.0 * sigma * sigma) ) / (.5 * (sigma_r + sigma_l) * SQ2PI)) * width
    

def ConvolveModel(r):
    convolvedModel = [0.0 for i in range(len(r))]
    for i in range(len(r)):
        for j in range(len(convolvedModel)):
            R = float(j+center_offset)
            #print j, ac.getg(float(j + offset + 1)) - ac.getg(float(j + offset))
            convolvedModel[j] += r[i] * StarConvolution(ac.getg(float(i)+center_offset) - ac.getg(float(j)+center_offset), float(i+center_offset), ac.getg(float(j + offset + 1)) - ac.getg(float(j + offset))) * R * R * R
    for i in range(len(convolvedModel)):
        convolvedModel[i] = convolvedModel[i] * sigmoid_error(ac.getg(float(i)+center_offset), 1) / ((float(i) + center_offset) * (float(i) + center_offset) * (float(i) + center_offset))# * float(341315437)
    return convolvedModel
    
def CreateObservedBackground(r, inputFile): 
    InitMWModel(Saved=inputFile)
    ReturnModel = np.array([[0.0 for k in range(len(this.FullSkyModel[0][0]))] for i in range(len(this.FullSkyModel[0]))])
    print r[0], r[1]
    for i in range(r[0]-offset, r[1]-offset):
        for j in range(len(ReturnModel)):
            for k in range(len(ReturnModel[j])):
                ReturnModel[j][k] += this.FullSkyModel[i][j][k]
    return ReturnModel

def InitMWModel(extent=None, bins=None, Saved=None, Observe = 0):
    this.FullSkyModel = []
    if Saved:
        f = open(Saved, 'rb')
        #R, RA, Dec
        this.FullSkyModel = np.array(pickle.load(f))
        f.close()
        if Observe:
            for i in range(len(this.FullSkyModel[0])):
                for j in range(len(this.FullSkyModel[0][0])):
                    print i, j
                    this.FullSkyModel[:, i, j] = ConvolveModel(this.FullSkyModel[:, i, j])
    else:
        
        r_range = np.linspace(offset, 65.0, 66-offset)
        print r_range
        for i in range(len(r_range)-1):
            this.FullSkyModel.append(CreateBackgroundDensity(extent, bins, [r_range[i], r_range[i+1]]))
        this.FullSkyModel = np.array(this.FullSkyModel)
        if Observe:
            for i in range(len(this.FullSkyModel[0])):
                for j in range(len(this.FullSkyModel[0][0])):
                    print i, j
                    this.FullSkyModel[:, i, j] = ConvolveModel(this.FullSkyModel[:, i, j])
        
    a = open("TestSave2_65kpc_BackConvolved.data", "wb")
    pickle.dump(this.FullSkyModel, a)
    a.close()
    return  


def TestPencilBeam():
    r_range = np.linspace(offset, 65.0, 66.0-offset)
    TestModel = []
    for i in range(len(r_range)-1):
        TestModel.append(CreateBackgroundDensity([[220, 221], [3, 4]], [1, 1], [r_range[i], r_range[i+1]]))
    TestModel = np.array(TestModel)
    TestModel = TestModel[:,0,0]
    
    convolvedModel = ConvolveModel(TestModel)
    
    total = 0.0
    for i in range(5):
        total += convolvedModel[i+7]
    print total
    
    print convolvedModel   
    plt.plot(range(offset,65), convolvedModel, 'ro')
    print len(TestModel)

    plt.plot(range(offset,65), TestModel, 'bo')
    plt.show() 
    return
    
def TestConvolution():
    TestPoint = [0.0 for i in range(offset, 65)]
    TestPoint[0] = 1.0
    #TestPoint[35] = 1.0
    convolvedModel = ConvolveModel(TestPoint)

    plt.plot(range(offset,65), convolvedModel, 'o')
    plt.show() 
    print sum(convolvedModel)
    return
    

def TestDetectionEfficiency(): 
    convolvedModel = [0.0 for i in range(offset, 65)]
    for i in range(len(convolvedModel)):
        convolvedModel[i] = sigmoid_error(ac.getg(float(i)+center_offset), 1)

    plt.plot(range(offset,65), convolvedModel, 'o')
    plt.show() 
    return

if __name__ == "__main__":
    #Test Functions
    #InitMWModel([[255, 260], [0, 5]], [10, 10], Observe=1)
    #InitMWModel([[120, 260], [-5, 35]], [280, 80], Observe=0)
    InitMWModel([[120, 260], [-5, 35]], [280, 80], Saved="TestSave2_65kpc.data", Observe=1)
    #TestConvolution()
    #TestDetectionEfficiency()
    #TestPencilBeam()
    #print np.linspace(3.0, 65.0, 63)



