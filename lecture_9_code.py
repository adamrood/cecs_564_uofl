import operator as op
from functools import reduce
import math
import numpy as np
import pandas as pd

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return (numer / denom) * math.factorial(r)

birthdays = []

for x in range(1,100):
    perm = ncr(365,x)
    birthdays.append([x, 1 - (perm/(365**x))])

df = pd.DataFrame(birthdays, columns=['# People','Probability'])
df.style.hide_index()