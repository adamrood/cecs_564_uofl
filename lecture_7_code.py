import numpy as np
import math
from functools import reduce

def cycles(n):
    x = np.random.permutation(n) + 1
    y = sorted(x)
    xy = list(zip(y,x))
    xyl = [list(a) for a in xy]
    print('')
    print('Permutation mapping:')
    stage = list(zip(*xyl))
    print(list(stage[0]))
    print(list(stage[1]))
    holding = []
    counts = []
    cycles = []
    start = 0
    while len(xyl) > 0:
        counter = 0
        holding.append(xyl.pop(0))
        counter += 1
        check = any(e[0] == holding[-1][1] for e in holding)
        while check == False:
            search = holding[-1][1]
            result = [element for element in xyl if element[0] == search]
            to_pop = xyl.index(result[0])
            holding.append(xyl.pop(to_pop))
            counter += 1
            check = any(e[0] == holding[-1][1] for e in holding)
        counts.append(counter)
        end = len(holding)
        cycles.append(holding[start:end])
        start = end
    print('')
    print('Cycle lengths:')
    print(counts)
    print('')
    print('Cycles:')
    for x in range(len(cycles)):
        print(cycles[x])
    lcm = reduce(lambda x,y: x*y // gcd(x,y), counts)
    print('')
    print('This is of order:', lcm)

cycles(3)
