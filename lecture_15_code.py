import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import numpy as np
import matplotlib.pyplot as plt

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

byt, seed = LFSR([0,0,0,1],[4,1])
print(byt)
print(seed)

s = [0,0,0,1]
k_list = []
for i in range(1000):
    k, b = LFSR(s,[4,1])
    k_list.append(k)
    s = b

plt.plot(k_list)
plt.show()
plt.plot(k_list[0:60])
plt.show()

s = [0,0,1,1,0,0,0,0,1,1,1,1]
k_list = []
for i in range(10000):
    k, b = LFSR(s,[12,6,4,1])
    k_list.append(k)
    s = b

plt.plot(k_list)
plt.show()
plt.plot(k_list[0:60])
plt.show()