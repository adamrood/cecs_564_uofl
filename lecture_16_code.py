import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import operator
from functools import reduce

path = 'U:\\Continuing_Education\\CECS_564-50\\Week_1\\'

with open(path + 'darwin.txt') as corpus:
    lines = corpus.read().splitlines()
darwin = ''.join(lines)
darwin = [ord(x) for x in darwin]

def LFSR(seed,c):
    m = len(c)
    n = len(seed)
    bt = []
    for k in range(8):
        bt.append(seed[n - 1])
        b = 0
        for i in range(m):
            b = b ^ seed[c[i] - 1]
        seed = np.roll(seed,1)
        seed[0] = b
    bt = str(''.join([chr(x + 48) for x in bt]))
    byt = int(bt,2)
    return byt, seed

def get_binary(c):
    stage_list = []
    character_list = [x for x in c]
    for x in range(len(character_list)):
        stage = format(ord(character_list[x]),'08b')
        stage_list.append([int(x) for x in stage])
    stage_list = reduce(operator.concat,stage_list)
    return stage_list

def histogram(ds):
    plt.hist(ds[0:10000],bins = 255)
    plt.show()

##LFSR(8)
s = get_binary('%')
poly = [8,4,3,2]
k = []

for i in range(10000):
    k_temp, b = LFSR(s,poly)
    k.append(k_temp)
    s = b

y = []
for x in range(10000):
    y.append(darwin[x] ^ k[::-1][x])

z = []
for x in range(10000):
    z.append(y[x] ^ k[::-1][x])

histogram(k[0:255])
histogram(darwin[0:255])
histogram(y[0:255])
histogram(z[0:255])