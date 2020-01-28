import numpy as np
import math
from functools import reduce

def Josephus(n, k):
    order = []
    mapping = []
    int_n = n
    n = list(np.arange(1, n + 1, 1))
    idx = k - 1
    while len(n) > 1:
        x = n.pop(idx)
        order.append(x)
        idx = (idx - 1 + k) % len(n)
    print ('The survivor is #',n[0])
    for x in range(len(order)):
        mapping.append([x + 1, order[x]])
    mapping.append([int_n, n[0]])
    print('')
    print('Cycle permutation:')
    print(sorted(mapping))
    #find order
    cycles = sorted(mapping)
    holding = []
    counts = []
    while len(cycles) > 0:
        counter = 0
        holding.append(cycles.pop(0))
        counter += 1
        check = any(e[0] == holding[-1][1] for e in holding)
        while check == False:
            search = holding[-1][1]
            result = [element for element in cycles if element[0] == search]
            to_pop = cycles.index(result[0])
            holding.append(cycles.pop(to_pop))
            counter += 1
            check = any(e[0] == holding[-1][1] for e in holding)
        counts.append(counter)
    print('')
    print('Cycle lengths:')
    print(counts)
    lcm = reduce(lambda x,y: x*y // gcd(x,y), counts)
    print('')
    print('This is of order:', lcm)

Josephus(41,3)
Josephus(90,2)

def Cut(n):
    cut_set = list(np.arange(1, n + 1, 1))
    idx = math.ceil(len(cut_set)/2)
    list1 = cut_set[idx:]
    list2 = cut_set[0:idx]
    print('')
    print('Cut')
    print(list1 + list2)

Cut(8)
Cut(9)

def Riffle(n):
    cut_set = list(np.arange(1, n + 1, 1))
    idx = math.ceil(len(cut_set)/2)
    list1 = cut_set[idx:]
    list2 = cut_set[0:idx]
    riffled = [val for pair in zip(list2, list1) for val in pair]
    if len(list1) != len(list2):
        riffled.append(list2[idx-1])
    print('')
    print('Riffle')
    print(riffled)

Riffle(8)
Riffle(9)