#!/usr/bin/python
import sys
import matplotlib
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.io import ascii
from operator import mul
import math as ma

def distance(g_0):
    return (10. ** ((g_0 - 4.2)/5.0) / 100.)*u.kpc 


data = ascii.read("../../Segue_weissj3_GPS1.csv", format='csv', fast_reader=True)


sc = SkyCoord(ra=[i*u.deg for i in data["ra_2"] ], dec=[i*u.deg for i in data["dec_2"]], distance=[15.0*u.kpc for i in data["g0"]], pm_ra_cosdec=[i*u.mas/u.yr for i in data["mura"]], pm_dec=[i * u.mas/u.yr for i in data["mudec"]], radial_velocity=[i * u.km/u.s for i in data["elodierv"]])

#print(sc.velocity)

totalvx = 0.0
totalvy = 0.0
totalvz = 0.0
totalx  = 0.0
totaly  = 0.0
totalz  = 0.0
n = 0

reduced_data = {"x":[], "y":[], "z":[], "v_x":[], "v_y":[], "v_z":[]}

for i in range(len(sc)):
    if data["elodierv"][i] > 200 or data["elodierv"][i] < -200 or data["mura err"][i] > 2.8 or data["mudec err"][i] > 2.8 : continue
    a = sc.galactocentric[i]
    reduced_data["x"].append(a.x.value)
    reduced_data["y"].append(a.y.value)
    reduced_data["z"].append(a.z.value)
    reduced_data["v_x"].append(a.v_x.value)
    reduced_data["v_y"].append(a.v_y.value)
    reduced_data["v_z"].append(a.v_z.value)

    totalvx += a.v_x
    totalvy += a.v_y
    totalvz += a.v_z
    b = sc.galactocentric[i]
    totalx  += b.x
    totaly  += b.y
    totalz  += b.z
    n += 1
    

avgvx = totalvx/float(n)
avgvy = totalvy/float(n)
avgvz = totalvz/float(n)
avgx = totalx/float(n)
avgy = totaly/float(n)
avgz = totalz/float(n)
print("Average Position")

print(avgx, avgy, avgz)

print("Average Velocity")

print(avgvx, avgvy, avgvz)
velMag = ma.sqrt(avgvx.value * avgvx.value + avgvy.value *avgvy.value + avgvz.value * avgvz.value)
print(velMag, avgvx / velMag, avgvy/velMag, avgvz/velMag)

plt.subplot(4,2,1)
plt.plot(reduced_data["v_x"], reduced_data["v_y"], "o", ms=0.5)
plt.xlim([-2000, 2000])
plt.ylim([-2000, 2000])
plt.xlabel("X Velocity (km/s)")
plt.ylabel("Y Velocity (km/s)")
plt.subplot(4,2,2)
plt.plot(reduced_data["v_y"], reduced_data["v_z"], "o", ms=0.5)
plt.xlim([-2000, 2000])
plt.ylim([-2000, 2000])
plt.xlabel("Y Velocity (km/s)")
plt.ylabel("Z Velocity (km/s)")
plt.subplot(4,2,3)
plt.plot(reduced_data["v_x"], reduced_data["v_z"], "o", ms=0.5)
plt.xlim([-2000, 2000])
plt.ylim([-2000, 2000])
plt.xlabel("X Velocity (km/s)")
plt.ylabel("Z Velocity (km/s)")
plt.subplot(4,2,4)
plt.hist(data["mura"], bins=30, alpha=0.5)
plt.hist(data["mudec"], bins=30,  alpha=0.5)
plt.subplot(4,2,5)
plt.plot(reduced_data["x"], reduced_data["y"], "o", ms=0.5)
#plt.xlim([-40, 40])
#plt.ylim([-40, 40])
plt.xlabel("X (kpc)")
plt.ylabel("Y (kpc)")
plt.subplot(4,2,6)
plt.plot(reduced_data["y"], reduced_data["z"], "o", ms=0.5)
#plt.xlim([-2000, 2000])
#plt.ylim([-2000, 2000])
plt.xlabel("Y (kpc)")
plt.ylabel("Z (kpc)")
plt.subplot(4,2,7)
plt.plot(reduced_data["x"], reduced_data["z"], "o", ms=0.5)
#plt.xlim([-2000, 2000])
#plt.ylim([-2000, 2000])
plt.xlabel("X (kpc)")
plt.ylabel("Z (kpc)")
plt.subplot(4,2,8, projection="aitoff")
plt.plot(sc.galactic.l.wrap_at(180*u.deg).radian, sc.galactic.b.radian, "o", ms=0.5)
plt.grid(True)
plt.show()
