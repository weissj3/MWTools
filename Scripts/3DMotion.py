#!/usr/bin/python
import sys
import matplotlib
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import astropy.units as u

r = 10. ** (20.337 - 4.2)/5.0 / 100.
sc = SkyCoord(ra=191.9772186*u.deg, dec=-8.5618715*u.deg, distance=r*u.kpc, pm_ra_cosdec=10.6677*u.mas/u.yr, pm_dec=-16.4151*u.mas/u.yr, radial_velocity=146.2*u.km/u.s)

print(sc.cartesian)
