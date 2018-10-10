import sys
import matplotlib.pyplot as plt

f = open(sys.argv[1], 'r')

g = []
gminr = []

f.readline()
for line in f:
    ln = map(float, line.split(','))
    if (ln[3] - ln[4]) < 0.4: continue
    g.append(ln[4])
    gminr.append(ln[4]-ln[5])    



plt.plot(gminr, g, 'o', ms=3)
plt.plot([0.1, 0.1], [16, 23], 'g', lw=2)
plt.plot([0.3, 0.3], [16, 23], 'g', lw=2)
plt.ylim([23, 16])
plt.xlim([0, 0.6])
plt.xlabel("$(g-r)_0$", fontsize=18)
plt.ylabel("$g_0$", fontsize=18)
plt.show()
