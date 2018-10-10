import math as ma
import matplotlib.pyplot as plt
import sys




def parallax_mag(x):
  return ma.log10(1.0/x * 100.) * 5.0 + 4.2

MatchingStars = []

if len(sys.argv) > 1:
    gaia = open("../Data/GaiaAndSDSSDisk/gaiatrimmed.csv", 'r')
    SDSS = open("../Data/GaiaAndSDSSDisk/48L51and10B12.csv", 'r')

    gaiaStars = [ ]
    SDSSStars = [ ]
    #l and be = 2 and 3
    for line in gaia:
        gaiaStars.append(map(float, line.split(',')))
    print len(gaiaStars)
        
    # l and b = 11 and 12
    for line in SDSS:
        ln = line.split(',')
        SDSSStars.append([float(ln[12]), float(ln[13])])
    print len(SDSSStars)
        


    for i in SDSSStars:
        for j in gaiaStars:
            if ma.sqrt(abs(i[0] - j[2]) * abs(i[0] - j[2]) + abs(i[1] - j[3]) * abs(i[1] - j[3]))  < 0.000277778:
                MatchingStars.append(j)
                break


    gaiaDone = open("../Data/GaiaAndSDSSDisk/GaiaMatched.csv", 'w')

    for i in MatchingStars:
        gaiaDone.write("%f, %f, %f, %f\n" % (i[0], i[1], i[2], i[3]))
    gaiaDone.close()

else:
    gaia = open("../Data/GaiaAndSDSSDisk/GaiaMatched.csv", 'r')
    for line in gaia:
        MatchingStars.append(map(float, line.split(',')))
    
    
    
    
mag  = []
for i in MatchingStars:
    mag.append(parallax_mag(i[0]))

plt.hist(mag, range=[16,23], bins = 28)
plt.show()
