import sys
sys.path.insert(0, '../Newby-tools/utilities')
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac
import operator
import MetalicityUtilities as met


if __name__ == "__main__":
    lbCuts = [[48.5, 52.], [68.5, 71.5], [92.5, 95.5], [108.5, 111.5], [128.5, 131.5], [148.5, 151.5], [176.5, 179.5], [185.5, 188.5], [201.5, 204.5], [227.5, 230.5]]
    file = sys.argv[1]
    fig, ax = plt.subplots(5,2)
    fig.tight_layout()
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

        print min(values[2]), max(values[2]), min(values[13]), max(values[13])
        plt.subplot(5,2,j)
        #plt.plot(map(float, values[12]), map(float, values[13]), 'o')
        plt.scatter(map(float, values[2]), map(float, values[13]), c=map(float, values[21]), s=10.0, linewidth=.1, edgecolor='gray')
        plt.imshow(met.averageMetallicities(values, [0., 4.5], [-30., 30.], [15, 24]), extent=[0., 4.5,-30, 30], interpolation='none', aspect='auto')    
        plt.xlabel("$Distance (kpc)$")
        plt.ylabel("B")
        plt.title("Metallicity at B and Distance (l between %.1f and %.1f)" % (lbCuts[j][0], lbCuts[j][1]))
        plt.colorbar()
    plt.show()
