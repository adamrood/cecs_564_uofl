import string
import re
from pycipher import Caesar, Affine, SimpleSubstitution
import matplotlib.pyplot as plt
import numpy as np
import statistics
from scipy import stats
from collections import Counter

path = 'U:\\Continuing_Education\\CECS_564-50\\Week_3\\'

def clean_text(filename):
    global cleaned_text
    with open(path + filename) as corpus:
        lines = corpus.read().splitlines()
    string = ''.join(lines)
    print('Pre-processing character count:  ' + str('{:,}'.format(len(string))))
    cleaned_text = re.sub('[^A-Za-z]+', '', string).lower()
    print('Post-processing character count: ' + str('{:,}'.format(len(cleaned_text))))
    print('')

clean_text('darwin.txt')

def affine_cipher(a, b):
    global encrypted_string
    print('Affine Cipher')
    print('Original string:  ' + str(cleaned_text[:75]))
    encrypted_string = Affine(a,b).encipher(cleaned_text)
    print('Encrypted string: ' + str(Affine(a,b).encipher(cleaned_text[:75])))
    print('Decrypted string: ' + str(Affine(a,b).decipher(Affine(a,b).encipher(cleaned_text[:75]))).lower())
    print('')

def shift_cipher(key):
    global encrypted_string
    print('Shift Cipher')
    print('Original string:  ' + str(cleaned_text[:75]))
    encrypted_string = Caesar(key = key).encipher(cleaned_text)
    print('Encrypted string: ' + str(Caesar(key = key).encipher(cleaned_text[:75])))
    print('Decrypted string: ' + str(Caesar(key = key).decipher(Caesar(key = key).encipher(cleaned_text[:75]))).lower())
    print('')

def substitution_cipher():
    global encrypted_string
    key = ''.join(np.random.choice([x for x in string.ascii_uppercase], 
        size = 26, replace = False))
    print('Substitution Cipher (key = ' + str(key) + ")" )
    print('Original string:  ' + str(cleaned_text[:75]))
    encrypted_string = SimpleSubstitution(key = key).encipher(cleaned_text)
    print('Encrypted string: ' + str(SimpleSubstitution(key = key).encipher(cleaned_text[:75])))
    print('Decrypted string: ' + str(SimpleSubstitution(key = key).decipher(SimpleSubstitution(key = key).encipher(cleaned_text[:75]))).lower())
    print('')

def summary_statistics(text):
    if text[0] != text[0].lower():
        values = [ord(x) - 65 for x in text]
    if text[0] == text[0].lower():
        values = [ord(x) - 97 for x in text]
    m = statistics.mean(values)
    s = statistics.stdev(values)
    e = stats.entropy(list(Counter(values).values()), base = 2)
    return m, s, e

def show_histogram():
    plt.hist([ord(x) - 97 for x in cleaned_text], bins = range(27), label = 'plaintext')
    plt.hist([ord(x) - 97 for x in encrypted_string.lower()], bins = range(27), label = 'ciphertext')
    plt.title('Histogram of letter distribution')
    plt.xlabel('letter')
    plt.legend(loc='upper right')
    plt.xticks(list(np.arange(0,26,1)),[x for x in string.ascii_lowercase])
    plt.ylabel('frequency')
    plt.show()

#shift summary statistics
shift_cipher(15)
summary_statistics(encrypted_string)
show_histogram()

#affine summary statistics
affine_cipher(21,18)
summary_statistics(encrypted_string)
show_histogram()

#clean text summary statistics (no encryption)
summary_statistics(cleaned_text)

#Substitution cipher
substitution_cipher()
summary_statistics(encrypted_string)