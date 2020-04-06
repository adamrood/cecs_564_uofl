def SquareAndMultiply(x, c, n):
    b = bin(c)[2:].zfill(32)
    m = len(b)
    z = 1
    for i in range(m):
        z = (z**2) % n
        if(b[i] == '1'):
            z = (z * x) % n 
    return z

SquareAndMultiply(9726, 3533, 11413)