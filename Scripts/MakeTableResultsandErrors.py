import sys

params = open(sys.argv[1], 'r')
errors = open(sys.argv[2], 'r')

error = []

for line in errors:
    if len(line) < 5: continue
    error.append(map(float, line.replace('[', '').replace(']', '').split(',')))


print error
output = []
count = 0
paramCount = 0
roundValues = [4, 2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1]
for line in params:
    out = ""
    ln = line.replace(' ', '').split(",")
    for i in range(len(ln)):
        if ln[i] == '\n': continue
        out += "$" + str(round(float(ln[i]), roundValues[paramCount])) + "\pm" + str(round(error[count][paramCount], roundValues[paramCount])) + "$ & "
        paramCount += 1
    output.append(out[0:len(out)-3])
#    print out[0:len(out)-3]
    if paramCount == 20:
        count += 1
        paramCount = 0

for i in output:
    print i
wedge = range(9,24)

for i in range(4):
    count = 0
    for j in range(len(output)/5 + 1):
        print str(wedge[count]) + " & " + output[j*5+i] + " \\\\"
        print "\hline"
        count += 1
print ""
