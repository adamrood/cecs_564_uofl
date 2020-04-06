import time

def SquareAndMultiply(x, c, n):
    b = bin(c)[2:].zfill(16)
    z = 1
    for i in range(len(b)):
        z = (z**2) % n
        if(b[i] == '1'):
            z = (z * x) % n
    return z

SquareAndMultiply(9726, 3533, 11413)

##Speed test
b = 97260000
e = 353300000
m = 11413
y = 1

t = time.time()
for i in range(e):
    y = (y * b) % m
elapsed = time.time() - t
print('elapsed:', elapsed, 'seconds')

t = time.time()
SquareAndMultiply(9726, 3533, 11413)
elapsed = time.time() - t
print('elapsed:', elapsed, 'seconds')
