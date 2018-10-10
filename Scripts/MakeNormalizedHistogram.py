import sys
import math as ma
import numpy as np

params = ["$\\varepsilon_{sph}$ & ", "$q$ & ", "$\\varepsilon$ & ", "$\mu$ & ", "R & ", "$\\theta$ & ", "$\phi$ &", " $\sigma$ & ", "$\\varepsilon$ & ", "$\mu$ & ", "R & ", "$\\theta$ & ", "$\phi$ & ", "$\sigma$ & ", "$\\varepsilon$ & ", "$\mu$ & ", "R & ", "$\\theta$ & ", "$\phi$ & ", "$\sigma$ & "] 


count = 0
for i in range(1, len(sys.argv)): 
    if i == 3 : count += 1; print "\cline{1-9}"
    if i == 9 : count += 1; print "\cline{1-1}\cline{4-15}"
    if i == 15 : count += 1; print "\cline{1-1} \cline{10-21}"
    
    a = [( ("%.2g" % k) if (abs(k) < 1000 and abs(k) > .01) else ("%.1e" % k)) for k in [j/(84046.0) for j in map(float, sys.argv[i].split())] ]
    a[i-1] = "\textbf{" + a[i-1] + "}" 
    placeholder = [ "& ---" for j in range(i+1, len(sys.argv)) ]
    if count == 0:
        placeholder[2-i] = "& \multicolumn{1}{|c}{---}"
    if count == 1:
        a[2] = "\multicolumn{1}{|c}{" + a[2] + "} "
        placeholder[8-i] = "& \multicolumn{1}{|c}{---}"
    if count == 2:
        a[8] = "\multicolumn{1}{|c}{" + a[8] + "}"
        placeholder[14-i] = "& \multicolumn{1}{|c}{---}"
    if count == 3:
        a[14] = "\multicolumn{1}{|c}{" + a[14] + "}"
    #print str(a[:i]).replace('[', '').replace(',', ' &').replace("'",'').replace(']', ' ')

    print  params[i-1] + str(a[:i]).replace('[', '').replace(',', ' &').replace("'",'').replace(']', ' ') + str(placeholder).replace('[', '').replace(',', '').replace("'",'').replace(']', '\\\\') 
