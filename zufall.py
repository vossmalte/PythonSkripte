# Visualisierung zum Zufall
import random
from visual.graph import *
def do(n=1000):
    k=0
    for i in range(n):
        if random.random()<.5:
            k+=1
    return k/n

gdisplay(background=color.white, foreground=color.black,ytitle="Anteil", xtitle="n")
w=gcurve()
for i in range(1, 10000):
    w.plot(pos=(i,do(i)))
