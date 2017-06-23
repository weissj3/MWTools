import sys
sys.path.insert(0, '../Newby-tools/utilities')
import math as ma
import matplotlib.pyplot as plt
import astro_coordinates as ac

def Create_Line(x0, x1, y0, y1):
    m = (y1 - y0)/(x1 - x0)
    b = y1 - m * x1
    return m,b
    


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
##########################################
###         Cut Lower Blob             ###
##########################################
line0x0 = 17.0
line0x1 = 19.75
line0y0 = -25.
line0y1 = 0.
line1x0 = 17.0
line1x1 = 19.75
line1y0 = -160.
line1y1 = -100.

m0, b0 = Create_Line(line0x0, line0x1, line0y0, line0y1)
m1, b1 = Create_Line(line1x0, line1x1, line1y0, line1y1)

x0 = []
x1 = []
for i in range(0,100):
    x0.append((line0x0 - line0x1) * i/100.0 + line0x1)
    x1.append((line1x0 - line1x1) * i/100.0 + line1x1)

y0 = [((m0 * i) + b0) for i in x0]
y1 = [((m1 * i) + b1) for i in x1]

############################################
###             Cut Upper Blob           ###
############################################
line2x0 = 17.7
line2x1 = 19.17
line2y0 = 50.0
line2y1 = 120.0
line3x0 = 17.7
line3x1 = 19.17
line3y0 = 120.
line3y1 = 200.

m2, b2 = Create_Line(line2x0, line2x1, line2y0, line2y1)
m3, b3 = Create_Line(line3x0, line3x1, line3y0, line3y1)

x2 = []
x3 = []
for i in range(0,100):
    x2.append((line2x0 - line2x1) * i/100.0 + line2x1)
    x3.append((line3x0 - line3x1) * i/100.0 + line3x1)

y2 = [((m2 * i) + b2) for i in x2]
y3 = [((m3 * i) + b3) for i in x3]






for i in range(len(values[0])):
    #if (values[26][i] > line1y0 and values[26][i] < line0y1 and float(values[3][i]) > line0x0 and float(values[3][i]) < line1x1 and values[26][i] < (m0 * float(values[3][i])) + b0 and values[26][i] > (m1 * float(values[3][i])) + b1):
    if (values[26][i] > -120. and values[26][i] < -25. and float(values[3][i]) > 16.8 and float(values[3][i]) < 17.8):
    #if (values[26][i] < -67.5 and values[26][i] > -120. and float(values[3][i]) > line0x0 and float(values[3][i]) < line1x1):
    #if (values[26][i] > line1y0 and values[26][i] < line0y1 and float(values[3][i]) > line0x0 and float(values[3][i]) < line1x1):
        for j in range(len(values)):
            CutValues[j].append(values[j][i])
    #if (values[26][i] > 50.0 and values[26][i] < 200. and float(values[3][i]) > 17.7 and float(values[3][i]) < 19.17 and values[26][i] > (m2 * float(values[3][i])) + b2 and values[26][i] < (m3 * float(values[3][i])) + b3):
    #    for j in range(len(values)):
    #        CutValues[j].append(values[j][i])

plt.subplot(2,2,1)
plt.plot(map(float, CutValues[10]), map(float, CutValues[11]), 'o', ms=1.2)
plt.xlim([110, 230])
plt.ylim([-5,60])
plt.xlabel("RA")
plt.ylabel("Dec")
plt.title("Remade Field of Streams")
ax = plt.gca()
ax.invert_xaxis()
plt.subplot(2,2,2)
plt.plot(map(float, CutValues[3]), map(float, CutValues[26]), 'o', ms=1.2)
plt.xlabel("$g_o$")
plt.ylabel("$v_{gsr}$")
plt.title("Stars in Cut")
plt.subplot(2,2,3)
plt.plot(map(float, values[3]), map(float, values[26]), 'o', ms=1.2)
plt.plot(x0, y0)
plt.plot(x1, y1)
plt.xlabel("$g_o$")
plt.ylabel("$v_{gsr}$")
plt.title("All Stars $v_{gsr}$ vs $g_o$")
plt.subplot(2,2,4)
plt.hist(map(float, CutValues[26]), bins=30) 
plt.ylabel("Counts")
plt.xlabel("$v_{gsr}$")
plt.title("Histogram of cut stars")
#plt.plot(x2, y2)
#plt.plot(x3, y3)
#plt.plot(map(float, values[3]), values[26], 'o', ms=1.2)
plt.show()
