import string
import re
from pycipher import Caesar
import matplotlib.pyplot as plt
import numpy as np
import math

path = 'U:\\Continuing_Education\\CECS_564-50\\Week_1\\'

def clean_text(filename):
    with open(path + filename) as corpus:
        lines = corpus.read().splitlines()
    string = ''.join(lines)
    print('Pre-processing character count:  ' + str('{:,}'.format(len(string))))
    cleaned_text = re.sub('[^A-Za-z]+', '', string).lower()
    print('Post-processing character count: ' + str('{:,}'.format(len(cleaned_text))))
    print('')
    return cleaned_text

def show_histogram(file):
    plt.hist(file, bins = range(27), label = 'character')
    #plt.hist([ord(y) - 97 for y in encrypted_string.lower()], bins = range(27), label = 'ciphertext')
    plt.title('Histogram of letter distribution')
    plt.xlabel('letter')
    plt.legend(loc='upper right')
    plt.xticks(list(np.arange(0,26,1)),[x for x in string.ascii_lowercase])
    plt.ylabel('frequency')
    plt.show()

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

def factor(x):
    list_factors = []
    for i in range(1, x + 1):
       if x % i == 0 and i != 1 and i != x:
           list_factors.append(i)
    return list_factors

def RSA_Encrypt(x, b, n):
    x = [ord(y) - 97 for y in x]
    while len(x) % 3 != 0:
        x.append(0)
    hub = []
    for i in range(len(x)):
        if int(i) % 3 == 0:
            temp = x[i:i + 3]
            hub.append(temp[0] * 26 * 26 + temp[1] * 26 + temp[2])
    enc_1 = []
    for j in range(len(hub)):
        t = SquareAndMultiply(hub[j],b,n)
        x1 = t % 26
        t = (t - x1) / 26
        x2 = t % 26
        x3 = (t - x2) / 26
        enc_1.append(int(x3))
        enc_1.append(int(x2))
        enc_1.append(int(x1))
    return enc_1

def RSA_Decrypt(x, b, n):
    hub = []
    for i in range(len(x)):
        if int(i) % 3 == 0:
            temp = x[i:i + 3]
            hub.append(temp[0] * 26 * 26 + temp[1] * 26 + temp[2])
    p1 = factor(n)
    p = p1[0]
    q = p1[1]
    phi = (p - 1) * (q - 1)
    s = ExtendedEuclidean(phi, b)
    a = s[2] % phi
    enc_1 = []
    for j in range(len(hub)):
        t = SquareAndMultiply(hub[j],a,n)
        x1 = t % 26
        t = (t - x1) / 26
        x2 = t % 26
        x3 = (t - x2) / 26
        enc_1.append(int(x3))
        enc_1.append(int(x2))
        enc_1.append(int(x1))
    return enc_1

##Use ONLY SquareAndMultiply for encryption/decryption
p = 2
q = 13
n = p*q
phi = (p-1)*(q-1)
b = 7
z = ExtendedEuclidean(phi, b)
a = z[2] % phi

x = clean_text('darwin.txt')
x_ord = [ord(y) - 97 for y in x]
show_histogram(x_ord)

#Encrypt using SquareAndMultiply
encrypted = []
for i in range(len(x_ord)):
    encrypted.append(SquareAndMultiply(x_ord[i], b, n))

show_histogram(encrypted)

#Decrypt using SquareAndMultiply
decrypted = []
for i in range(len(encrypted)):
    decrypted.append(SquareAndMultiply(encrypted[i], a, n))

##Not at all secure!
print(''.join([chr(x + 97) for x in x_ord[0:30]]))
print(''.join([chr(x + 97) for x in encrypted[0:30]]))
print(''.join([chr(x + 97) for x in decrypted[0:30]]))

#RSA Encryption and decryption
x = clean_text('darwin.txt')
p = 19
q = 919
n = p * q
b = 9871

e = RSA_Encrypt(x, b, n)
show_histogram(z)

d = RSA_Decrypt(e, b, n)
show_histogram(d)

print(x[0:30])
print(''.join([chr(x + 97) for x in e[0:30]]))
print(''.join([chr(x + 65) for x in d[0:30]]))