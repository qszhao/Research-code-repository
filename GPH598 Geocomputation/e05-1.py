# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import random
import math
pi = math.pi 
z = raw_input('Please enter the convergence criterion: ')
criterion = float(z)
j = raw_input('Please enter the sentinel value: ')
value = int(j)

n = 0 # number of points falling in the unit circle
d = 0 # number of points falling in the unit square
i = 0
while i<=value:
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1.0:
        n += 1
    d += 1
    ratio = 4 * n * 1./d
    print ratio
    i+=1
    if i>value:
        k= abs(ratio-pi) / pi
        print "The draw limit is exceeded."
        print "The percentage difference between the current estimate of Pi is %f, and the true value is %f" %(k,ratio)
    if abs(ratio-pi) / pi <= criterion:
        print "Draws needed: ", d
        break

# <codecell>


