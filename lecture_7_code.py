import numpy as np
import math
from functools import reduce
from collections import Counter
import pandas as pd

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
    lcm = reduce(lambda x,y: x*y // math.gcd(x,y), counts)
    print('')
    print('This is of order:', lcm)

cycles(5)
cycles(7)
cycles(41)

##Code to create table of Group/Permutation Count/Order.
##Code functions well for small n size (<= 12)

##function to find all unique summations of a given number
def sum_to_n(n, size, limit=None):
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail

##create list of groups
def create_table(n):
    groups = ['e']
    values = [1]
    orders = [1]
    for x in range(1,n):
        for group in sum_to_n(n, x):
            groups.append(group)
    #removing 1 values for simplicity
    groups_reduced = [[ele for ele in sub if ele != 1] for sub in groups]
    for a in range(1, len(groups_reduced)):
        first_stop = []
        n2 = n
        for y in range(len(groups_reduced[a])):
            work = []
            for q in range(groups_reduced[a][y]):
                work.append(n2)
                n2 -= 1
            first_stop.append(np.product(work)/len(work))
        if len(groups_reduced[a]) != len(set(groups_reduced[a])):
            mult_list = []
            multipliers = []
            for x in Counter(groups_reduced[a]).items():
                if x[1] != 1:
                    multipliers.append(x[1])
            for x in multipliers:
                mult_list.append(1/math.factorial(x))
            values.append(np.product(first_stop)*np.product(mult_list))
        else:
            values.append(np.product(first_stop))
        orders.append(reduce(lambda x,y: x*y // math.gcd(x,y), groups_reduced[a]))
    if np.sum(values) == math.factorial(n):
        return pd.DataFrame(list(zip(groups,values,orders)), columns = ['Structure','Count','Order'])
    else:
        return 'An error occured.  You likely entered a value that is too big to compute.'

create_table(5) #class example
create_table(7) #homework assignment
create_table(12) #stress test