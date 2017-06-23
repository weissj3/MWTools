import sys
sys.path.insert(0, '../Newby-tools/utilities')
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac
import operator

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
    plt.plot(map(float, values[12]), map(float, values[13]), 'o')
    plt.show()
