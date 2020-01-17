from pycipher import Affine
import numpy as np
import math

##Find coprime numbers
def coprime(a,b):
    return math.gcd(a,b) == 1

##Get list of relative prime numbers
def get_set(z):
    set_list = []
    for x in range(0,z):
        if coprime(x,z):
            set_list.append(x)
    return set_list

##Get all pairs of multiplicated inverse
def get_pairs(z):
    pairs = []
    rp_set = get_set(z)
    for x in rp_set[:]:
        for y in rp_set[:]:
            if (x*y) % z == 1:
                pairs.append((x,y))
    pairs = [sorted(x) for x in pairs]
    print(sorted(set(map(tuple, pairs))))
    
##Calculate Euler's Number (phi(m)) -- This doesn't quite match what we did in class, 
##but it follows the same principal
def get_set_size(z):
    set_list = []
    for x in range(0,z):
        if coprime(x,z):
            set_list.append(x)
    return len(set_list)

print(get_set_size(26))
print(get_set_size(256))

##Number of keys in Z26 for Affine cipher
b = 26
print('There are ' + str(get_set_size(b) * b) + ' possible keys in Affine Cipher.')

##Exhaustive Search for Affine cipher example
plaintext = 'cryptography'
##Set possible a and b values
a = get_set(26)
b = np.arange(0,26,1)
##Encrypt message -- selecting arbitrary keys 7 and 20
encrypted_message = Affine(7,20).encipher(plaintext)
print(encrypted_message)
##Loop through values of a and b until we find the key
for x in a:
    for y in b:
        check = Affine(x,y).decipher(encrypted_message)
        if check == plaintext.upper():
            break
    if check == plaintext.upper():
        print(x,y)
        print(check, plaintext.upper())
        break

##Trivial keys for Affine cipher
for b in range(26):
    if b == (-1*b % 26):
        print((1 % 26,-1*b % 26))

##Involuntary keys for Affine cipher (Not 100% sure on this)
##Get multiplicative inverses
get_pairs(26)
##For an Involuntary key in Affine cipher, a must equal a^-1, 
##so that narrows it down to a = 1 and a = 25
a = [1,25]
b = np.arange(0,26,1)
for v in a:
    for w in b:
        if v*1+w % 26 == v*(1-w) % 26:
            print((v,w))

##Extended Euclidean Algorithm
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

##Class examples
print(ExtendedEuclidean(75,26))
print((-9*75)+(26*26))

print(ExtendedEuclidean(75,256))
print((99*75)+(-29*256))

print(ExtendedEuclidean(256,75))
print((-29*256)+(99*75))

print(ExtendedEuclidean(17,26))
print(-3*17 % 26)

print(ExtendedEuclidean(211,256))
print(91*211 % 256)

print(ExtendedEuclidean(76,256))