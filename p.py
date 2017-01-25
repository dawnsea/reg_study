#!/usr/bin/python
import matplotlib
matplotlib.use("TkAgg")


import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import norm
import scipy.stats as stats

print math.e
def frange(x, y, jump):
    r = []
    
    while x <= y:
        r.append(x)
        x += jump

    return r

def logi(l):
    e = math.e

    r = []

    for v in l:
        r.append(e ** v / (1.0 + e ** v))

    return r

def gumi(l):
    e = math.e
    for v in l:
        r.append(e ** ((-e) ** v))

    return r

xx = frange(-10, 10, 0.1)
yy = logi(xx)

print 'mean = ', np.mean(yy)
print 'std = ', np.std(yy)

plt.plot(xx, yy)
plt.show()

