import sys
import math as ma
sys.path.insert(0, '../Newby-tools/utilities')
import astro_coordinates as ac
import operator as op
def stars(eps1, eps2, eps3, num_stars):
    starsPerComponent = [ 0,0,0,0 ]
    denom = 1.0 / (1.0 + ma.exp(eps1) + ma.exp(eps2) + ma.exp(eps3))
    starsPerComponent[0] = int(round(num_stars * denom,0))
    starsPerComponent[1] = int(round(num_stars * ma.exp(eps1) * denom,0))
    starsPerComponent[2] = int(round(num_stars * ma.exp(eps2) * denom,0))
    starsPerComponent[3] = int(round(num_stars * ma.exp(eps3) * denom,0))
    return starsPerComponent

params = open(sys.argv[1], 'r')
integrals = open(sys.argv[2], 'r')

output = []
count = 0
paramCount = 0
roundValues = [4, 2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1]
num_stars = [95435, 97939, 97434, 120612, 118836, 102599, 108460, 107033, 91626, 95462, 84046, 105909, 60503, 66200, 65355]
bgParameters = []
streamParameters = [] #eps, mu, r, t, p, sig, stars, A, l, b
bgIntegral = []
streamIntegrals = []

count = 0
for line in params:
    if line == '\n': continue
    ln = map(float,line.split())
    if len(ln) == 2:
        bgParameters.append(ln)
    else:
        streamParameters.append(ln)
#    print ln

for line in integrals:
    if line == '\n': continue
    ln = map(float, line.split())
    if len(ln) == 1:
        bgIntegral.append(ln[0])
    else:
        streamIntegrals.append(ln)
#    print ln

for i in range(0,len(streamParameters), 3):
    a = stars(streamParameters[i][0], streamParameters[i+1][0], streamParameters[i+2][0], num_stars[i/3])
    print a
    #AppendNumberOfStars
    bgParameters[i/3].append(a[0])
    streamParameters[i].append(a[1])
    streamParameters[i+1].append(a[2])
    streamParameters[i+2].append(a[3])
    #AppendAValues
    bgParameters[i/3].append(a[0]/bgIntegral[i/3])
    streamParameters[i].append(a[1]/streamIntegrals[i/3][0])
    streamParameters[i+1].append(a[2]/streamIntegrals[i/3][1])
    streamParameters[i+2].append(a[3]/streamIntegrals[i/3][2])
    #MU, NU, R, Wedge
    for j in range(3):
        templ, tempb, tempr = ac.GC2lbr(streamParameters[i+j][1], 0.0, streamParameters[i+j][2], i/3+9)
        streamParameters[i+j].append(templ)
        streamParameters[i+j].append(tempb)
        streamParameters[i+j].append(map(op.sub, ac.stream2xyz(0, 0, 1,  streamParameters[i+j][1], streamParameters[i+j][2], streamParameters[i+j][3] * ac.deg, streamParameters[i+j][4]*ac.deg,  i/3+9), ac.stream2xyz(0, 0, 0,  streamParameters[i+j][1], streamParameters[i+j][2], streamParameters[i+j][3]*ac.deg, streamParameters[i+j][4]*ac.deg,  i/3+9)))

#Print backgrounds (Stripe, Stars, A, q, r_0, espheroid)
for i in range(len(bgParameters)):
    print "$" + str(i + 9) + "$ & $" + str(bgParameters[i][2]) + "$ & $" + str(int(round(bgParameters[i][3], 0))) + "$ & $" + str(round(bgParameters[i][1], 2)) + "$ & $" +  str(12.0) + "$ & $" +  str(round(bgParameters[i][0], 4)) + "$ \\\\"
    print "\hline"

print "******************************************************"
#Print Streams
for i in range(3):
    for j in range(0, len(streamParameters), 3):
        print "$" + str(j/3 + 9) + "$ & $" + str(streamParameters[j + i][6]) + "$ & $" + str(round(streamParameters[j + i][8], 1)) + "$ & $" + str(round(streamParameters[j + i][9], 1)) + "$ & $" + str(round(streamParameters[j + i][2], 1)) + "$ & $" + str(round(streamParameters[j + i][7], 1)) + "$ & $" +  str(round(streamParameters[j + i][5], 1)) + "$ & $" +  str(tuple(map(round, streamParameters[j + i][10], [2,2,2]))) + "$ \\\\"
        print "\hline"
    print "******************************************************"
        
        
        
#        out += "$" + str(round(float(ln[i]), roundValues[paramCount])) + "\pm" + str(round(error[count][paramCount], roundValues[paramCount])) + "$ & "
#        paramCount += 1
#    output.append(out[0:len(out)-3])
#    print out[0:len(out)-3]
#    if paramCount == 20:
#        count += 1
#        paramCount = 0

#for i in output:
#    print i
#wedge = range(9,24)

#for i in range(4):
#    count = 0
#    for j in range(len(output)/5 + 1):
#        print str(wedge[count]) + " & " + output[j*5+i] + " \\\\"
#        print "\hline"
#        count += 1
#print ""
