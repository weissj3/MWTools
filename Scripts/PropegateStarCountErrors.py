import sys
import math as ma

eps1 = ma.exp(float(sys.argv[1]))
eps2 = ma.exp(float(sys.argv[2]))
eps3 = ma.exp(float(sys.argv[3]))
err1 = float(sys.argv[4])
err2 = float(sys.argv[5])
err3 = float(sys.argv[6])
stars = int(sys.argv[7])

denom = 1.0 + eps1 + eps2 + eps3

fbg = 1.0 / denom
f1 = eps1 / denom
f2 = eps2 / denom
f3 = eps3 / denom

print "Stars:"
print "BG: " + str(fbg * stars)
print "Str1: " + str(f1 * stars)
print "Str2: " + str(f2 * stars)
print "Str3: " + str(f3 * stars)

errBG = ((eps1 / (denom * denom)) ** 2) * err1 * err1 + (eps2/(denom*denom)**2) * err2 * err2 + (eps3/(denom*denom)**2) * err3 * err3
errStars1 = ((((1. + eps2 + eps3) * eps1) / (denom * denom)) ** 2) * err1 * err1 + ((eps2*eps1)/(denom*denom)**2) * err2 * err2 + ((eps3*eps1)/(denom*denom)**2) * err3 * err3
errStars2 = ((((1. + eps1 + eps3) * eps2) / (denom * denom)) ** 2) * err2 * err2 + ((eps1*eps2)/(denom*denom)**2) * err1 * err1 + ((eps3*eps2)/(denom*denom)**2) * err3 * err3
errStars3 = ((((1. + eps2 + eps1) * eps3) / (denom * denom)) ** 2) * err3 * err3 + ((eps2*eps3)/(denom*denom)**2) * err2 * err2 + ((eps3*eps1)/(denom*denom)**2) * err1 * err1

print "Errors: "
print "BG: " + str(ma.sqrt(errBG) * stars)
print "Str1: " + str(ma.sqrt(errStars1) * stars)
print "Str2: " + str(ma.sqrt(errStars2) * stars)
print "Str3: " + str(ma.sqrt(errStars3) * stars)
