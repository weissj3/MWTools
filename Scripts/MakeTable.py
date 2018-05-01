import sys

fname = sys.argv[1]
f = open(sys.argv[1], 'r')

for line in f:
    out = ""
    ln = line.split(", ")
    for i in ln:
        if i == '\n': continue 
        out += "$" + str(round(float(i), 2)) + "$ & "
    print out[0:len(out)-3]
