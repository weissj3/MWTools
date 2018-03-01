#!/usr/bin/python
import sys
import matplotlib
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.io import ascii
from operator import mul

def distance(g_0):
    return (10. ** ((g_0 - 4.2)/5.0) / 100.)*u.kpc 


data = ascii.read("../../Segue_weissj3_GPS1.csv", format='csv', fast_reader=True)

sc = SkyCoord(ra=[i*u.deg for i in data["ra_2"] ], dec=[i*u.deg for i in data["dec_2"]], distance=[distance(i) for i in data["g0"]], pm_ra_cosdec=[i*u.mas/u.yr for i in data["mura"]], pm_dec=[i * u.mas/u.yr for i in data["mudec"]], radial_velocity=[i * u.km/u.s for i in data["elodierv"]])

print(sc.velocity)
plt.subplot(2,2,1)
plt.plot(sc.velocity.d_x, sc.velocity.d_y, "o", ms=0.5)
plt.xlim([-2000, 2000])
plt.ylim([-2000, 2000])
plt.xlabel("X Velocity (km/s)")
plt.ylabel("Y Velocity (km/s)")
plt.subplot(2,2,2)
plt.plot(sc.velocity.d_y, sc.velocity.d_z, "o", ms=0.5)
plt.xlim([-2000, 2000])
plt.ylim([-2000, 2000])
plt.xlabel("Y Velocity (km/s)")
plt.ylabel("Z Velocity (km/s)")
plt.subplot(2,2,3)
plt.plot(sc.velocity.d_x, sc.velocity.d_z, "o", ms=0.5)
plt.xlim([-2000, 2000])
plt.ylim([-2000, 2000])
plt.xlabel("X Velocity (km/s)")
plt.ylabel("Z Velocity (km/s)")
plt.show()
