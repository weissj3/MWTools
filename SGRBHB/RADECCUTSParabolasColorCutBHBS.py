import sys
sys.path.insert(0, '../Newby-tools/utilities')
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac
import operator

def ParabolaParams(x1, y1, x2, y2, x3, y3):
    a = (x3*(y2-y1) + x2*(y1-y3) + x1*(y3-y2))/((x1 - x2) * (x1 - x3) * (x2 - x3))
    b = ((x1 * x1) * (y2- y3) + (x3 * x3) * (y1 - y2) + (x2 * x2) * (y3 - y1))/((x1 - x2) * (x1 - x3) * (x2 - x3))
    c = ((x2 * x2) * (x3 * y1 - x1 * y3) + x2 * (x1 * x1 * y3 - x3 * x3 * y1) + (x1 * x3) * (x3 - x1) * y2)/((x1 - x2) * (x1 - x3) * (x2 - x3))
    return a, b, c

def Parabola(a, b, c, x):
    return a * x * x + b * x + c


file = sys.argv[1]
f = open(file,"r")

cols = f.readline().split(",")
values = []
for i in cols:
    values.append([])

for line in f:
    ln = line.split(",")
    for i in range(len(ln)):
        values[i].append(ln[i])

#for i in range(len(objID)):
#    for j in range(i+1, len(objID)):
#        if objID[i] == objID[j]:
#            print objID[i]

values.append(map(ac.rv_to_vgsr, map(float,values[23]), map(float,values[12]), map(float,values[13])))
CutValues = []
CutValues2 = []
for i in range(len(values)):
    CutValues.append([])
    CutValues2.append([])


a1, b1, c1 = ParabolaParams(140., 17., 170., 13., 200., 0.)
a2, b2, c2 = ParabolaParams(140., 23., 170., 20., 220., 0.)
a3, b3, c3 = ParabolaParams(140., 34., 180., 25., 220., 8.)
a4, b4, c4 = ParabolaParams(140., 29., 180., 18., 220., 3.)

minimum=120.
maximum=140.

ra = []
dec = []

for i in range(130, 240):
    tempRA, tempDEC = ac.GCToEq(float(i), 0.0, 19)
    ra.append(tempRA)
    dec.append(tempDEC)

x = []
y1 = []
y2 = []
y3 = []
y4 = []

for i in range(110, 230):
    x.append(float(i))
    y1.append(Parabola(a1, b1, c1, float(i)))
    y2.append(Parabola(a2, b2, c2, float(i)))
    y3.append(Parabola(a3, b3, c3, float(i)))
    y4.append(Parabola(a4, b4, c4, float(i)))

for i in range(len(values[0])):
    #if 100.0 > ((float(values[10][i]) - 190.0)**2.0 + (float(values[11][i]) - 10.0)**2.0):
    uming = (float(values[1][i]) - float(values[7][i])) - (float(values[2][i]) - float(values[8][i]))
    if (uming < .8) or (uming > 1.5) or values[26][i] < -1000.: continue;
    if float(values[11][i]) > Parabola(a1, b1, c1, float(values[10][i])) and float(values[11][i]) < Parabola(a2, b2, c2, float(values[10][i])) and float(values[10][i]) < maximum and float(values[10][i]) > minimum:
        for j in range(len(values)):
            CutValues[j].append(values[j][i])
    if float(values[11][i]) < Parabola(a3, b3, c3, float(values[10][i])) and float(values[11][i]) > Parabola(a4, b4, c4, float(values[10][i])) and float(values[10][i]) < maximum and float(values[10][i]) > minimum:
        for j in range(len(values)):
            CutValues2[j].append(values[j][i])

plt.subplot(3,2,1)
plt.plot(map(float, CutValues[10]), map(float, CutValues[11]), 'o', ms=1.2) #, c=map(float, CutValues[26]), cmap=plt.cm.get_cmap('RdYlBu'), linewidths=0, s=5.0)
#plt.colorbar()
ax = plt.gca()
ax.invert_xaxis()
plt.xlabel("RA")
plt.ylabel("Dec")
plt.title("Sagittarius Cut (%d to %d)" % (minimum, maximum))
plt.subplot(3,2,3)
plt.plot(map(operator.sub, map(float, CutValues[3]), map(float, CutValues[8])), map(float, CutValues[26]), 'o', ms=1.2)
plt.title("$v_{gsr}$ vs $g_o$ (Sagittarius)")
plt.xlabel("$g_o$")
plt.ylabel("$v_{gsr}$")
plt.ylim([-300, 300])
plt.xlim([15, 22])
plt.subplot(3,2,2)
plt.plot(map(float, CutValues2[10]), map(float, CutValues2[11]), 'o', ms=1.2)#, c=map(float, CutValues2[26]), cmap=plt.cm.get_cmap('RdYlBu'), linewidths=0, s=5.0)
#plt.colorbar()
ax = plt.gca()
ax.invert_xaxis()
plt.xlabel("RA")
plt.ylabel("Dec")
plt.title("Bifurcated Stream Cut (%d to %d)" % (minimum, maximum))
plt.subplot(3,2,4)
plt.plot(map(operator.sub, map(float, CutValues2[3]), map(float, CutValues2[8])), map(float, CutValues2[26]), 'o', ms=1.2)
plt.title("$v_{gsr}$ vs $g_o$ (Bifurcated Stream)")
plt.xlabel("$g_o$")
plt.ylabel("$v_{gsr}$")
plt.ylim([-300, 300])
plt.xlim([15, 22])
plt.subplot(3,2,5)
plt.plot(map(float, values[10]), map(float, values[11]), 'o', ms=1.2)#, c=map(float,values[26]), cmap=plt.cm.get_cmap('gist_heat'), linewidths=0, s=5.0, vmin=-130., vmax=0.)
#plt.colorbar()
plt.xlim([120, 220])
plt.ylim([-5, 55])
ax = plt.gca()
ax.invert_xaxis()
plt.title("Repulled Data Newberg Color Cut BHB Stars")
plt.xlabel("RA")
plt.ylabel("Dec")
plt.plot(ra, dec)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
ra1, dec1 = ac.GCToEq(170., 0.0, 19)
plt.plot(ra1, dec1, 'o')
#plt.plot(x0, y0)
#plt.plot(x1, y1)
#plt.plot(x2, y2)
#plt.plot(x3, y3)
#plt.plot(map(float, values[3]), values[26], 'o', ms=1.2)
plt.show()
