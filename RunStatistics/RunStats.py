import math as ma
import sys
import matplotlib.pyplot as plt

file = sys.argv[1]
f = open(file,"r")

line = f.readline();
while(line[0] != 'T'):
    line = f.readline()

average = []
stddev = []
parameters = []
for i in range(21):
    average.append(0.0)
    stddev.append(0.0)
    parameters.append([])
for line in f:
    line = line.replace("[", "")
    line = line.replace("]", "")
    line = line.replace("'", "")
    line = line.replace("\t", "")
    line = line.replace("\n", "")
    ln = line.split(", ")
    for i in range(1, len(ln)-1):
        parameters[i-1].append(float(ln[i]))

#compute Average
for i in range(len(parameters)):
    for j in parameters[i]:
        average[i] += j
for i in range(len(average)):
    average[i] = average[i]/len(parameters[0])

for i in range(len(parameters)):
    for j in parameters[i]:
        diff = (j - average[i])
        stddev[i] += diff*diff

for i in range(len(stddev)):
    stddev[i] = ma.sqrt(stddev[i] / float(len(parameters[i])))
    

print "Min, Max, Median, Average, Stddev"
for i in range(len(parameters)):
    parameters[i].sort()
    print parameters[i][0], parameters[i][len(parameters[i])-1], parameters[i][len(parameters[i])/2], average[i], stddev[i]

plt.hist( parameters[16], bins=15)
plt.show()



