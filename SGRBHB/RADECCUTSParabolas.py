import sys
sys.path.insert(0, '../Newby-tools/utilities')
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac
import operator


def Create_Line(x0, x1, y0, y1):
    m = (y1 - y0)/(x1 - x0)
    b = y1 - m * x1
    return m,b

def ParabolaParams(x1, y1, x2, y2, x3, y3):
    a = (x3*(y2-y1) + x2*(y1-y3) + x1*(y3-y2))/((x1 - x2) * (x1 - x3) * (x2 - x3))
    b = ((x1 * x1) * (y2- y3) + (x3 * x3) * (y1 - y2) + (x2 * x2) * (y3 - y1))/((x1 - x2) * (x1 - x3) * (x2 - x3))
    c = ((x2 * x2) * (x3 * y1 - x1 * y3) + x2 * (x1 * x1 * y3 - x3 * x3 * y1) + (x1 * x3) * (x3 - x1) * y2)/((x1 - x2) * (x1 - x3) * (x2 - x3))
    return a, b, c

def Parabola(a, b, c, x):
    return a * x * x + b * x + c

def ColorCutStars(stars):
    line0x0 = -.3
    line0y0 = .9
    line0x1 = -.25
    line0y1 = 1.02
    m0,b0 = Create_Line(line0x0, line0x1, line0y0, line0y1)    

    line1x0 = -.25
    line1y0 = 1.02
    line1x1 = -.15
    line1y1 = 1.15
    m1,b1 = Create_Line(line1x0, line1x1, line1y0, line1y1)      

    line2x0 = -.15
    line2y0 = 1.15
    line2x1 = 0.
    line2y1 = 1.1
    m2,b2 = Create_Line(line2x0, line2x1, line2y0, line2y1)   

    BHBs = []
    BlueStragglers = []
    for i in range(len(stars)):
        BHBs.append([])
        BlueStragglers.append([])

    for i in range(len(stars[0])):
        gminr= ((float(stars[2][i]) - float(stars[8][i])) - (float(stars[3][i]) - float(stars[9][i])))
        uming= ((float(stars[1][i]) - float(stars[7][i])) - (float(stars[2][i]) - float(stars[8][i])))
        if gminr > -.3 and gminr < -.25:
            if uming > m0 * gminr + b0:
                for j in range(len(stars)):
                    BHBs[j].append(stars[j][i])
                    continue
            else:
                for j in range(len(stars)):
                    BlueStragglers[j].append(stars[j][i])
                    continue
        elif gminr > -.25 and gminr < -.15:
            if uming > m1 * gminr + b1:
                for j in range(len(stars)):
                    BHBs[j].append(stars[j][i])
                    continue
            else:
                for j in range(len(stars)):
                    BlueStragglers[j].append(stars[j][i])
                    continue
        elif gminr > -.15 and gminr < 0.:
            if uming > m2 * gminr + b2:
                for j in range(len(stars)):
                    BHBs[j].append(stars[j][i])
                    continue
            else:
                for j in range(len(stars)):
                    BlueStragglers[j].append(stars[j][i])
                    continue
    return BHBs, BlueStragglers
        
def RADECCUT(stars, minimum=120., maximum=220.):
    StarsWithinSGR = []
    StarsWithinBif = []
    for i in range(len(stars)):
        StarsWithinSGR.append([])
        StarsWithinBif.append([])
    a1, b1, c1 = ParabolaParams(140., 17., 170., 13., 200., 0.)
    a2, b2, c2 = ParabolaParams(140., 23., 170., 20., 220., 0.)
    a3, b3, c3 = ParabolaParams(140., 34., 180., 25., 220., 8.)
    a4, b4, c4 = ParabolaParams(140., 29., 180., 18., 220., 3.)

    for i in range(len(stars[0])):
        if float(stars[11][i]) > Parabola(a1, b1, c1, float(stars[10][i])) and float(stars[11][i]) < Parabola(a2, b2, c2, float(stars[10][i])) and float(stars[10][i]) < maximum and float(stars[10][i]) > minimum:
            for j in range(len(stars)):
                StarsWithinSGR[j].append(stars[j][i])
        if float(stars[11][i]) < Parabola(a3, b3, c3, float(stars[10][i])) and float(stars[11][i]) > Parabola(a4, b4, c4, float(stars[10][i])) and float(stars[10][i]) < maximum and float(stars[10][i]) > minimum:
            for j in range(len(stars)):
                StarsWithinBif[j].append(stars[j][i])
    return StarsWithinSGR, StarsWithinBif



def TestPlotColorColorDiagram(stars):
    line0x0 = -.3
    line0y0 = .9
    line0x1 = -.25
    line0y1 = 1.02
    m0,b0 = Create_Line(line0x0, line0x1, line0y0, line0y1)    

    line1x0 = -.25
    line1y0 = 1.02
    line1x1 = -.15
    line1y1 = 1.15
    m1,b1 = Create_Line(line1x0, line1x1, line1y0, line1y1)      

    line2x0 = -.15
    line2y0 = 1.15
    line2x1 = 0.
    line2y1 = 1.1
    m2,b2 = Create_Line(line2x0, line2x1, line2y0, line2y1)  
    x1 = []
    x2 = []
    x3 = []
    y1 = []
    y2 = []
    y3 = []
    for i in range(100):
        temp = -.3 + float(i) / 100. * .3 
        if temp < -.25:
            x1.append(temp)
            y1.append(m0 * temp + b0)
        if temp > -.25 and temp < -.15:
            x2.append(temp)
            y2.append(m1 * temp + b1)
        if temp > -.15:
            x3.append(temp)            
            y3.append(m2 * temp + b2)

    plt.plot(map(operator.sub, map(operator.sub, map(float, stars[2]), map(float, stars[8])), map(operator.sub, map(float, stars[3]), map(float, stars[9]))), map(operator.sub, map(operator.sub, map(float, stars[1]), map(float, stars[7])), map(operator.sub, map(float, stars[2]), map(float, stars[8]))), 'o', ms=1.2)
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.plot(x3, y3)
    
    ax = plt.gca()
    ax.invert_yaxis()
    plt.show()
    return

if __name__ == "__main__":
    file = sys.argv[1]
    f = open(file,"r")

    cols = f.readline().split(",")
    values = []
    for i in cols:
        values.append([])

    for line in f:
        ln = line.split(",")
        for i in range(len(ln)):
            values[i].append(ln[i])

    values.append(map(ac.rv_to_vgsr, map(float,values[23]), map(float,values[12]), map(float,values[13])))

    BHBs, BlueStars = ColorCutStars(values)
    
    minimum=200.
    maximum=220.

    BHBSGR, BHBBif = RADECCUT(BHBs, minimum, maximum)
    BlueSGR, BlueBif = RADECCUT(BlueStars, minimum, maximum)



    ra = []
    dec = []

    for i in range(130, 240):
        tempRA, tempDEC = ac.GCToEq(float(i), 0.0, 19)
        ra.append(tempRA)
        dec.append(tempDEC)

    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    a1, b1, c1 = ParabolaParams(140., 17., 170., 13., 200., 0.)
    a2, b2, c2 = ParabolaParams(140., 23., 170., 20., 220., 0.)
    a3, b3, c3 = ParabolaParams(140., 34., 180., 25., 220., 8.)
    a4, b4, c4 = ParabolaParams(140., 29., 180., 18., 220., 3.)
    for i in range(110, 230):
        x.append(float(i))
        y1.append(Parabola(a1, b1, c1, float(i)))
        y2.append(Parabola(a2, b2, c2, float(i)))
        y3.append(Parabola(a3, b3, c3, float(i)))
        y4.append(Parabola(a4, b4, c4, float(i)))

    #TestPlotColorColorDiagram(values)



    plt.subplot(3,2,1)
    plt.plot(map(float, BHBSGR[10]), map(float, BHBSGR[11]), 'o', ms=1.5)
    plt.plot(map(float, BlueSGR[10]), map(float, BlueSGR[11]), 'o', ms=1.5)
    ax = plt.gca()
    ax.invert_xaxis()
    plt.xlabel("RA")
    plt.ylabel("Dec")
    plt.title("Sagittarius Cut (%d to %d)" % (minimum, maximum))
    plt.subplot(3,2,3)
    plt.plot(map(operator.sub, map(float, BHBSGR[2]), map(float, BHBSGR[8])), map(float, BHBSGR[26]), 'o', ms=1.5)
    plt.title("$v_{gsr}$ vs $g_o$ (Sagittarius) BHBs")
    plt.xlabel("$g_o$")
    plt.ylabel("$v_{gsr}$")
    plt.ylim([-300, 300])
    plt.xlim([15, 22])
    plt.subplot(3,2,5)
    plt.plot(map(operator.sub, map(float, BlueSGR[2]), map(float, BlueSGR[8])), map(float, BlueSGR[26]), 'o', ms=1.5)
    plt.title("$v_{gsr}$ vs $g_o$ (Sagittarius) Blue Stragglers")
    plt.xlabel("$g_o$")
    plt.ylabel("$v_{gsr}$")
    plt.ylim([-300, 300])
    plt.xlim([15, 22])
    plt.subplot(3,2,2)
    plt.plot(map(float, BHBBif[10]), map(float, BHBBif[11]), 'o', ms=1.5)
    plt.plot(map(float, BlueBif[10]), map(float, BlueBif[11]), 'o', ms=1.5)
    ax = plt.gca()
    ax.invert_xaxis()
    plt.xlabel("RA")
    plt.ylabel("Dec")
    plt.title("Biffurcated Stream Cut (%d to %d)" % (minimum, maximum))
    plt.subplot(3,2,4)
    plt.plot(map(operator.sub, map(float, BHBBif[2]), map(float, BHBBif[8])), map(float, BHBBif[26]), 'o', ms=1.5)
    plt.title("$v_{gsr}$ vs $g_o$ (Biffurcated Stream) BHBs")
    plt.xlabel("$g_o$")
    plt.ylabel("$v_{gsr}$")
    plt.ylim([-300, 300])
    plt.xlim([15, 22])
    plt.subplot(3,2,6)
    plt.plot(map(operator.sub, map(float, BlueBif[2]), map(float, BlueBif[8])), map(float, BlueBif[26]), 'o', ms=1.5)
    plt.title("$v_{gsr}$ vs $g_o$ (Biffurcated Stream) Blue Stragglers")
    plt.xlabel("$g_o$")
    plt.ylabel("$v_{gsr}$")
    plt.ylim([-300, 300])
    plt.xlim([15, 22])

















    #plt.plot(map(float, values[10]), map(float, values[11]), 'o', ms=1.2)#, c=map(float,values[26]), cmap=plt.cm.get_cmap('gist_heat'), linewidths=0, s=5.0, vmin=-130., vmax=0.)
    #plt.colorbar()
    #plt.xlim([120, 220])
    #plt.ylim([-5, 55])
    #ax = plt.gca()
    #ax.invert_xaxis()
    #plt.title("All Blue Stars")
    #plt.xlabel("RA")
    #plt.ylabel("Dec")
    #plt.plot(ra, dec)
    #plt.plot(x, y1)
    #plt.plot(x, y2)
    #plt.plot(x, y3)
    #plt.plot(x, y4)
    #ra1, dec1 = ac.GCToEq(170., 0.0, 19)
    #plt.plot(ra1, dec1, 'o')
    #plt.plot(x0, y0)
    #plt.plot(x1, y1)
    #plt.plot(x2, y2)
    #plt.plot(x3, y3)
    #plt.plot(map(float, values[3]), values[26], 'o', ms=1.2)
    plt.show()
