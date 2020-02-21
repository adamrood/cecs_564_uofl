import numpy as np
import math
from numpy import matrix
from numpy import linalg
import re

path = 'U:\\Continuing_Education\\CECS_564-50\\Week_1\\'

def clean_text(filename):
    global cleaned_text
    with open(path + filename) as corpus:
        lines = corpus.read().splitlines()
    string = ''.join(lines)
    print('Pre-processing character count:  ' + str('{:,}'.format(len(string))))
    cleaned_text = re.sub('[^A-Za-z]+', '', string).lower()
    print('Post-processing character count: ' + str('{:,}'.format(len(cleaned_text))))
    print('')
    return cleaned_text

def modMatInv(A,p):
  n=len(A)
  A=matrix(A)
  adj=np.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(linalg.det(A))),p)*adj)%p

def modInv(a,p):
  for i in range(1,p):
    if (i*a)%p == 1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):
  A = np.array(A)
  minor = np.zeros(shape=(len(A) - 1, len(A) - 1))
  p=0
  for s in range(len(minor)):
    if p==i:
      p = p + 1
    q = 0
    for t in range(len(minor)):
      if q == j:
        q = q + 1
      minor[s][t] = A[p][q]
      q = q + 1
    p  =p + 1
  return minor

def generate(x,y):
    global k, k_1
    flag = 0
    while flag == 0:
        try:
            k = np.random.randint(y,size=(x,x))
            k_1 = modMatInv(k, 26)
            flag = 1
        except:
            continue
    return k, k_1.astype(int)

def hill_cipher(x, k, m):
    x1 = [ord(y.lower()) - 97 for y in x]
    it = 0
    ops = []
    while it < len(x):
        check = x1[it:it+len(k)]
        if len(check) != len(k):
            check = check + list(np.zeros(len(k) - len(check)).astype(int))
        ops.append(np.dot(check,k) % m)
        it = it + len(k)
    output = ''.join([chr(x + 65) for x in np.concatenate(ops,axis = 0)])[0:len(x1)]
    return output

##This is not quite perfect -- misses the last few characters.  Will work
##on this later
k, k_1 = generate(2,26)
darwin = clean_text('darwin.txt')[0:75]
print(darwin)
encrypted = hill_cipher(darwin[0:75],k,26)
print(encrypted)
decrypted = hill_cipher(encrypted,k_1,26)
print(decrypted.lower())