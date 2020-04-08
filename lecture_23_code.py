import math

def SquareAndMultiply(x, c, n):
    b = bin(c)[2:].zfill(16)
    z = 1
    for i in range(len(b)):
        z = (z**2) % n
        if(b[i] == '1'):
            z = (z * x) % n
    return z

def ExtendedEuclidean(a,m):
    q0, q1, r0, r1, s0, s1, t0, t1 = 0, 0, a, m, 1, 0, 0, 1
    r = 99
    while r != 0:
        q = math.floor(r0/r1)
        r = r0 - (q * r1)
        s = s0 - (q * s1)
        t = t0 - (q * t1)
        q0, q1, r0, r1, s0, s1, t0, t1 = q1, q, r1, r, s1, s, t1, t
    return ((a*s0) + (m*t0)), s0, t0

SquareAndMultiply(2398, 1261, 18923)

ph = (127-1)*(149-1) 
print(ph)

ExtendedEuclidean(ph,1261)
##greatest common divisor, weight1, weight2.....weight2 = a for decryption

print(1261*5797 % ph)
##1

SquareAndMultiply(4557, 5797, 18923)