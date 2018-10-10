#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
import matplotlib
import matplotlib.pyplot as plt
import csv
from files import read_data
import math as ma

eps0 = [-0.889337151903579, -0.789667771066783, -0.689360109873075, -1.44926529642484, -1.29742362304287, -1.42173073692646, -1.39158237927307, -1.1913619446896, -2.04457383309629, -0.358121422715121, -0.975790648804962, -1.51434905387913, -0.228005057763552, -1.08022635369968]
eps1 = [-1.17006771229324, -0.826987878216294, -2.04795848853281, -1.12274698202124, -1.00841949985378, -1.03188937256826, -0.621588116390597, -0.89593886727663, -1.40175262311727, -1.92984684016586, -2.34530413379031, -1.09552604987667, -0.876033827063212, -1.17316517187324]
eps2 = [-0.52846338492124, -1.4622495376852, -0.770969660487988, -0.87746090822167, -3.06999548292362, -1.7344360686712, -1.77476344486079, -4.36908111193551, -0.934586115434938, -0.995422534687567, -2.12619310049914, -1.71041665080847, -2.37933426251476, -3.00331544009593]
stars = [97939, 97434, 120612, 118836, 102599, 108460, 107033, 91626, 95462, 84046, 105909, 60503, 66200, 65355]
wedgeStart = 10


for i in range(14):

    denom = 1.0 + ma.exp(eps0[i]) + ma.exp(eps1[i]) + ma.exp(eps2[i])

    bg = 1.0 / denom * stars[i]
    str0 = ma.exp(eps0[i]) / denom * stars[i] + bg
    str1 = ma.exp(eps1[i]) / denom * stars[i] + str0
    str2 = ma.exp(eps2[i]) / denom * stars[i] + str1

    star_array4 = read_data("../../ResimSky_2/AllStars/AllSkyRebuildStars%d.txt" % (i + 10), delimiter=None, ignore="---", igval=float("Nan"), splitter=None, skip=1, echo=0)
    star_array = [star_array4[0:bg], star_array4[bg:str2]]

    output = ["../../ResimSky_2/SeparatedComponents/BG%d.txt" % (i + wedgeStart), "../../ResimSky_2/SeparatedComponents/Streams_%d.txt" % (i + wedgeStart)]

    for i in range(len(output)):
      f = open(output[i], "w")
      for j in star_array[i]:
        a = list(j)

        f.write(str(a[0]) + ", " + str(a[1]) + ", " + str(a[2]) +'\n')
      f.close()

