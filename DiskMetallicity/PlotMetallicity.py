import sys
sys.path.insert(0, '../Newby-tools/utilities')
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac
import operator

def getPosition(bounds, value, bins):
    return int((value - bounds[0]) / (bounds[1] - bounds[0]) * (bins))


def CutL(L_low, L_high, stars):
    tempStars = []    
    for i in range(len(stars)):
        tempStars.append([])

    for i in range(len(stars[0])):
        if float(stars[12][i]) < L_high and float(stars[12][i]) > L_low and float(stars[21][i]) > -9999.:
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
        x = getPosition(x_bounds, float(stars[2][i]) - float(stars[8][i]), bins[0])
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
    
    #values = CutL(48.5, 52., values)
    #values = CutL(68.5, 71.5, values)
    #values = CutL(92.5, 95.5, values)
    values = CutL(108.5, 111.5, values)

    #plt.plot(map(float, values[12]), map(float, values[13]), 'o')
    plt.scatter(map(operator.sub, map(float, values[2]), map(float, values[8])), map(float, values[13]), c=map(float, values[21]), edgecolor='gray')
    plt.imshow(averageMetallicities(values, [12.5, 23.], [-30., 30.], [30, 30]), extent=[12.5, 23,-30, 30], interpolation='none', aspect='auto')    
    plt.xlabel("$g_o$")
    plt.ylabel("B")
    plt.title("Metallicity at B and $g_o$")
    plt.colorbar()
    plt.show()
