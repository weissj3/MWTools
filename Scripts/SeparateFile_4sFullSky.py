#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
import matplotlib
import matplotlib.pyplot as plt
import csv
from files import read_data
import math as ma

eps0 = [-1.05212006486569, -1.6976338004683, -0.888944389648721, -2.8001590388523, -1.09160930960738, -0.71402577034935, -1.46539567277386, -2.51383149587712, -0.926829149179624, -0.254005346691466, -2.62192263910359, -2.90996552007396, -2.0696158677271, -3.76475121916234]
eps1 = [-0.742915790256845, -0.582770208647833, -0.724582036318793, -1.55014974675235, -2.82483755239157, -1.25085794998668, -2.27758115404744, -0.900535499386604, -2.23781336229453, -1.02618696122732, -2.88625547769572, -2.19996726856449, -2.07499872091103, -1.39164325487219]
eps2 = [-2.01820145685768, -0.953318687452432, -2.03447483056717, -0.643293126556657, -1.8336608031598, -1.96438393723851, -0.554329530897026, -2.75423598819487, -1.38515132749219, -2.00722657013353, -1.3344598260616, -0.917719451353255, -0.284112302516076, -1.09522752374112]
eps3 = [-0.633541757545494, -2.04229016230907, -2.09646941348786, -1.50693976686302, -1.68757951416455, -3.18763090388417, -2.54775556429175, -1.51136853853904, -3.78598079549598, -3.04697576940009, -1.05869486462999, -0.94170122716435, -0.717718196796108, -2.91079766220954]
stars = [97939, 97434, 120612, 118836, 102599, 108460, 107033, 91626, 95462, 84046, 105909, 60503, 66200, 65355]
wedgeStart = 10


for i in range(14):

    denom = 1.0 + ma.exp(eps0[i]) + ma.exp(eps1[i]) + ma.exp(eps2[i]) + ma.exp(eps3[i])

    bg = 1.0 / denom * stars[i]
    str0 = ma.exp(eps0[i]) / denom * stars[i] + bg
    str1 = ma.exp(eps1[i]) / denom * stars[i] + str0
    str2 = ma.exp(eps2[i]) / denom * stars[i] + str1
    str3 = ma.exp(eps3[i]) / denom * stars[i] + str2

    star_array4 = read_data("../../ResimSky_2/4sAllStars/AllSkyRebuildStars4Stream%d.txt" % (i + 10), delimiter=None, ignore="---", igval=float("Nan"), splitter=None, skip=1, echo=0)
    star_array = [star_array4[0:bg], star_array4[bg:str2]]

    output = ["../../ResimSky_2/4sSeparatedComponents/BG%d.txt" % (i + wedgeStart), "../../ResimSky_2/4sSeparatedComponents/Streams_%d.txt" % (i + wedgeStart)]

    for i in range(len(output)):
      f = open(output[i], "w")
      for j in star_array[i]:
        a = list(j)

        f.write(str(a[0]) + ", " + str(a[1]) + ", " + str(a[2]) +'\n')
      f.close()

