import sys

for i in range(1, len(sys.argv)):
    print [(j/(329.0 * 1.41)) for j in map(float, sys.argv[i].split())]
