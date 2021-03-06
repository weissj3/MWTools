import sys
import math as ma

likelihood = [-3.135414049, -3.13600654, -3.078028044, -3.078931874, -3.177612315, -3.178166425, -3.186226232, -3.186710685, -2.962983203, -2.963375301, -2.972523155, -2.972765512, -2.991625452, -2.991693258, -2.978142031, -2.978828116, -2.992593667, -2.99264534, -2.963790443, -2.963989179, -2.983413106, -2.984454222, -2.88509588, -2.885483708, -2.927664878, -2.927971068, -2.922835259, -2.923129871]
stars      = [97939, 97434, 120612, 118836, 102599, 108460, 107033, 91626, 95462, 84046, 105909, 60503, 66200, 65355]

def calculateBIC(likelihood, stars, parameters):
    return parameters * ma.log(stars) - 2.0 * stars * likelihood
    

for i in range(0, len(likelihood), 2):
    print calculateBIC(likelihood[i], stars[i/2], 26) - calculateBIC(likelihood[i+1], stars[i/2], 20)


