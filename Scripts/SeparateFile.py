#!/usr/bin/python
import sys
import matplotlib
import matplotlib.pyplot as plt
import csv
import sdss_visualizers as vis
from files import read_data
import math as ma

eps0 = float(sys.argv[1])
eps1 = float(sys.argv[2])
eps2 = float(sys.argv[3])
stars = int(sys.argv[4]
wedge = int(sys.argv[5])

denom = 1 + ma.exp(eps0) + ma.exp(eps1) + ma.exp(eps2)


bg = 1.0 / denom * stars
str0 = ma.exp(eps0) / denom * stars + bg
str1 = ma.exp(eps1) / denom * stars + str1
str2 = ma.exp(eps2) / denom * stars + str2

star_array4 = read_data(input4, delimiter=None, ignore="---", igval=float("Nan"), splitter=None, skip=1, echo=0)
star_array0 = star_array4[0:bg]
star_array1 = star_array4[bg:str0]
star_array2 = star_array4[str0:str1]
star_array3 = star_array4[str1:str2]

vis.plot_separation_mur(wedge, star_array0, star_array1, star_array2, star_array3, star_array4, outname=output, mag=0, scale=1, color=1, mu_lim=[135, 230], r_lim=(0, 49), vm=10, nu_flatten=0)
