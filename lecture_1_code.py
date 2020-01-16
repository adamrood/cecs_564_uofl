import string
import re
from pycipher import Caesar
import matplotlib.pyplot as plt
import numpy as np

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

def print_cypher(key, charcount):
    print('Original string:  ' + str(cleaned_text[0:charcount]))
    print('Encrypted string: ' + str(Caesar(key = key).encipher(cleaned_text)[0:charcount]))
    print('Decrypted string: ' + str(Caesar(key = key).decipher(Caesar(key = key).encipher(cleaned_text))[0:charcount]))
    print('')

def show_histogram():
    plt.hist([ord(x) - 97 for x in cleaned_text], bins = range(27))
    plt.title('Histogram of letter distribution')
    plt.xlabel('letter')
    plt.xticks(list(np.arange(0,26,1)),[x for x in string.ascii_lowercase])
    plt.ylabel('frequency')
    plt.show()

clean_text('darwin.txt')
print_cypher(23,75)
show_histogram()