gaia = open("../Data/GaiaAndSDSSDisk/gaialbcut.csv", 'r')
gaiaOutput = open("../Data/GaiaAndSDSSDisk/gaiatrimmed.csv", 'w')


gaia.readline()

# parallax = 9 parallax_over_error = 11 l = 73 b = 74

for line in gaia:
    ln = line.split(',')
    if ln[11] != '' and float(ln[11]) > 5.0:
        gaiaOutput.write("%f, %f, %f, %f\n" % (float(ln[9]), float(ln[11]), float(ln[73]), float(ln[74])))
        
gaiaOutput.close()
