import sys
import math as ma

#stars = [ma.sqrt(95435), ma.sqrt(97939), ma.sqrt(97434), ma.sqrt(120612), ma.sqrt(118836), ma.sqrt(102599), ma.sqrt(108460), ma.sqrt(107033), ma.sqrt(91626), ma.sqrt(95462), ma.sqrt(84046), ma.sqrt(105909), ma.sqrt(60503), ma.sqrt(66200), ma.sqrt(65355)]



#for i in range(1, len(sys.argv)):
print [(j/(ma.sqrt(84046)*ma.sqrt(2))) for j in map(float, sys.argv[1].split())]
