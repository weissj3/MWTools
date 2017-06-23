import sys
sys.path.insert(0, '../Newby-tools/utilities')
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac

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
for i in range(len(values)):
    CutValues.append([])





for i in range(len(values[0])):
    #if 100.0 > ((float(values[10][i]) - 190.0)**2.0 + (float(values[11][i]) - 10.0)**2.0):
    if 100.0 > ((float(values[10][i]) - 160.0)**2.0 + (float(values[11][i]) - 25.0)**2.0):
        for j in range(len(values)):
            CutValues[j].append(values[j][i])

plt.subplot(3,1,1)
plt.plot(map(float, CutValues[10]), map(float, CutValues[11]), 'o', ms=1.2)
ax = plt.gca()
ax.invert_xaxis()
plt.xlabel("RA")
plt.ylabel("Dec")
plt.title("Circle Cut (170, 15) With 5 Degree Radius")
plt.subplot(3,1,2)
plt.plot(map(float, CutValues[3]), map(float, CutValues[26]), 'o', ms=1.2)
plt.title("$v_{gsr}$ vs $g_o$")
plt.xlabel("$g_o$")
plt.ylabel("$v_{gsr}$")
plt.subplot(3,1,3)
plt.plot(map(float, values[10]), map(float, values[11]), 'o', ms=1.2)
ax = plt.gca()
ax.invert_xaxis()
plt.title("All BHBs")
plt.xlabel("RA")
plt.ylabel("Dec")
#plt.plot(x0, y0)
#plt.plot(x1, y1)
#plt.plot(x2, y2)
#plt.plot(x3, y3)
#plt.plot(map(float, values[3]), values[26], 'o', ms=1.2)
plt.show()
