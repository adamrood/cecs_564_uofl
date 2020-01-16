import string
import re
from pycipher import Affine, Caesar
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

path = 'U:\\Continuing_Education\\CECS_564-50\\Week_2\\'

def clean_text(filename):
    global cleaned_text
    with open(path + filename) as corpus:
        lines = corpus.read().splitlines()
    string = ''.join(lines)
    print('Pre-processing character count:  ' + str('{:,}'.format(len(string))))
    cleaned_text = re.sub('[^A-Za-z]+', '', string).lower()
    print('Post-processing character count: ' + str('{:,}'.format(len(cleaned_text))))
    print('')

def affine_cipher(a, b):
    print('Affine Cipher')
    print('Original string:  ' + str(cleaned_text))
    print('Encrypted string: ' + str(Affine(a,b).encipher(cleaned_text)))
    print('Decrypted string: ' + str(Affine(a,b).decipher(Affine(a,b).encipher(cleaned_text))).lower())
    print('')

def shift_cipher(key):
    print('Shift Cipher')
    print('Original string:  ' + str(cleaned_text))
    print('Encrypted string: ' + str(Caesar(key = key).encipher(cleaned_text)))
    print('Decrypted string: ' + str(Caesar(key = key).decipher(Caesar(key = key).encipher(cleaned_text))).lower())
    print('')

def AttackShift(enstr):         
    letter_freq_message = Counter([x for x in enstr])
    count_string = len(enstr)

    message_array = []
    for x in [x for x in string.ascii_uppercase]:
        message_array.append(letter_freq_message[x]/count_string)

    analyze_sad = []
    analyze_ss = []
    analyze_dp = []

    for x in range(1,26):
        analyze_sad.append(sum(abs(np.subtract(message_array,np.roll(letter_freq_master,x)))))
        analyze_ss.append(sum(abs(np.subtract(message_array,np.roll(letter_freq_master,x)**2))))
        analyze_dp.append(sum(abs(np.multiply(message_array,np.roll(letter_freq_master,x)))))

    print('Minimum sum absolute difference (sad) corresponds to key : ' + str(analyze_sad.index(min(analyze_sad)) + 1))
    print('Minimum sum of squares (ss) corresponds to key : ' + str(analyze_ss.index(min(analyze_ss)) + 1))
    print('Maximum dot product (dp) corresponds to key : ' + str(analyze_dp.index(max(analyze_dp)) + 1))
    print('')

##Preprocess text
clean_text('vote.txt')
##Example of Shift Cipher
shift_cipher(25)
##Example of Affine Cipher
affine_cipher(23,14)

##Encrypt text -- Full text, set of first 10 characters, set of next 10 characters
##These were the examples used in Lecture 3
encrypted_text = Caesar(25).encipher(cleaned_text)
encrypted_text_1_10 = Caesar(25).encipher(cleaned_text[0:10])
encrypted_text_11_20 = Caesar(25).encipher(cleaned_text[10:20])

##Exhaustive approach
for key in range(0,26):
    print('Decrypted string for key = ' + str(key) + ': ' 
    + str(Caesar(key = key).decipher(encrypted_text).lower()))

print('')

##From Table 1.1 of Cryptography Theory and Practice - Stinson, 3rd ed.
letter_freq_master = [.082,.015,.028,.043,.127,.022,.020,.061,.070,.002,.008,.040,
                      .024,.067,.075,.019,.001,.060,.063,.091,.028,.010,.023,.001,.020,.001]

##Curve fitting
AttackShift(encrypted_text)
AttackShift(encrypted_text_1_10)
AttackShift(encrypted_text_11_20)