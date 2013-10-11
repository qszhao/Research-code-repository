# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import random
import math
import numpy

def montecarlo(criteria):
    pi = math.pi 
    n = 0 # number of points falling in the unit circle
    d = 0 # number of points falling in the unit square
    simulating = True # use as a sentinel
    while simulating:
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            n += 1
        d += 1
        ratio = 4 * n * 1./d
        if abs(ratio-pi) / pi <= criteria:
            return d
            break
        
def statistic(x):
    l=[]
    for i in range(10):
        d=montecarlo(x)
        l.append(d)
        a= numpy.average(l)
        b= numpy.std(l)
    print "When criteria is equal to %f, the average number of draws is %f, the standard of the number of draws is %f" %(x,a,b)

statistic(0.01)
statistic(0.001)
statistic(0.0001)
statistic(0.00001)

# <codecell>


# <codecell>

|

# <codecell>


