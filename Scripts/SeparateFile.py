#!/usr/bin/python
import sys
sys.path.insert(0, '../Newby-tools/utilities')
import matplotlib
import matplotlib.pyplot as plt
import csv
from files import read_data
import math as ma

eps0 = float(sys.argv[1])
eps1 = float(sys.argv[2])
eps2 = float(sys.argv[3])
stars = int(sys.argv[4])
inputFile = sys.argv[5]
wedge = int(sys.argv[6])
output = [sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10]]


denom = 1 + ma.exp(eps0) + ma.exp(eps1) + ma.exp(eps2)


bg = 1.0 / denom * stars
str0 = ma.exp(eps0) / denom * stars + bg
str1 = ma.exp(eps1) / denom * stars + str0
str2 = ma.exp(eps2) / denom * stars + str1

star_array4 = read_data(inputFile, delimiter=None, ignore="---", igval=float("Nan"), splitter=None, skip=1, echo=0)
star_array = [star_array4[0:bg], star_array4[bg:str0], star_array4[str0:str1], star_array4[str1:str2]]

for i in range(len(output)):
  f = open(output[i], "w")
  for j in star_array[i]:
    a = list(j)

    f.write(str(a[0]) + ", " + str(a[1]) + ", " + str(a[2]) +'\n')
  f.close()

