
import math
import numpy as np
from astropy.table import Table
from astropy.io import ascii

x = np.linspace(0,(2 * np.pi ), 1000)
y = []

for i in x:
    y.append(math.sin(i))

data = Table([x,y],names=['x','sin(x)'])
ascii.write(data, 'newtable.txt', format='commented_header')
data_in = ascii.read('newtable.txt')
print(data_in)

