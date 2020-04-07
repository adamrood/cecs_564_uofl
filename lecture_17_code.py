import numpy as np
import binascii
import matplotlib.pyplot as plt
import string

path = 'U:\\Continuing_Education\\CECS_564-50\\Week_9\\'

def KeySchedule(k):
    keys = []
    master_keys = []
    key = [x for x in k]
    for x in range(len(key)):
        if ord(key[x]) < 16:
            keys.append(''.join(hex(ord(key[x])).split('x')))
        else:
            keys.append(''.join(hex(ord(key[x])).split('x'))[1:3])
    keys = ["{0:08b}".format(int(x, 16)) for x in keys]
    keys = [x for x in ''.join(keys)]
    x = 0 
    for n in range(5):
        master_keys.append(''.join(np.roll(keys,x)[0:16]))
        x -= 4
    return master_keys

def load_data(filename):
    with open(path + filename) as corpus:
        lines = corpus.read()
    input_data = []
    for x in range(len(lines)):
        input_data.append(lines[x])
    if len(input_data) % 2 == 1:
        input_data.append('x')
    else:
        next
    input_data = ''.join([x for x in input_data])
    return input_data

def text_to_bits(text, encoding='latin-1', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='latin-1', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def hex_to_bits(character):
    return bin(int(character,16))[2:].zfill(4)

def show_histogram(ds):
    plt.hist(ds,bins = 256)
    plt.title('Histogram')
    plt.xlabel('character')
    plt.ylabel('frequency')
    plt.show()

def encrypt_round():
    global w, v, key_set
    for kn in range(5):
        if kn != 4:
            y = int(key_set[kn], 2) ^ int(w, 2)
        else:
            y = int(key_set[kn], 2) ^ int(v, 2)
        if kn != 4:
            temp_xor = ''.join(hex(int(bin(y)[2:].zfill(len(key_set[kn])),2))[2:])
            if len(temp_xor) != 4:
                temp_xor = temp_xor.zfill(4)
            temp_v = []
            for x in temp_xor:
                temp_v.append(PS[int(x, 16)])
            v = ''.join([hex_to_bits(x) for x in ''.join(temp_v)])
        else:
            next
        if kn != 4:
            temp_w = []
            for x in range(len(v)):
                temp_w.append(v[int(PP[x],16)])
            w = ''.join(temp_w)
        else:
            next
    character_return = text_from_bits(bin(y)[2:].zfill(len(key_set[kn])))
    if len(character_return) == 1:
        character_return = character_return + np.random.choice([x for x in string.printable])
    return character_return

def decrypt_round():
    global w, v, u, key_set
    for kn in range(5):
        if kn == 0:
            next
        else:
            w = int(key_set[kn], 2) ^ int(u, 2)
        if kn != 4:
            if kn == 0:
                v = bin(int(key_set[kn], 2) ^ int(w, 2))[2:].zfill(16)
            else:
                temp_v = []
                for x in range(len(bin(w)[2:].zfill(16))):
                    temp_v.append(bin(w)[2:].zfill(16)[int(IPP[x],16)])
                v = ''.join(temp_v)
            temp_xor = hex(int(v,2))[2:]
            if len(temp_xor) != 4:
                temp_xor = temp_xor.zfill(4)
            temp_u = []
            for x in temp_xor:
                temp_u.append(IPS[int(x, 16)])
            u = ''.join([hex_to_bits(x) for x in ''.join(temp_u)])
    character_return = text_from_bits(bin(w)[2:].zfill(len(key_set[kn])))
    return character_return

def SPN_Encrypt(file, key):
    global encoded, key_set, w, PS, PP, input_text
    encoded = []
    key_set = KeySchedule(key)
    input_text = load_data(file)
    PS = 'e4d12fb83a6c5907'
    PP = '048c159d26ae37bf'
    for x in range(len(input_text) - 1):
        if x % 2 == 0:
            w = ''.join([text_to_bits(q) for q in input_text[x:x + 2]])
            encoded.append(encrypt_round())
    encoded = ''.join([x for x in encoded])

def SPN_Decrypt(file, key):
    global decoded, key_set, w, IPS, IPP
    decoded = []
    key_set = KeySchedule(key)
    key_set.reverse()
    input_text = encoded
    IPS='e3481caf7d96b205'
    IPP='048c159d26ae37bf'
    for x in range(len(input_text) - 1):
        if x % 2 == 0:
            w = ''.join([text_to_bits(q) for q in input_text[x:x + 2]])
            decoded.append(decrypt_round())
    decoded = ''.join([x for x in decoded])

SPN_Encrypt('wizard_of_oz.txt', 'xX7b')
SPN_Decrypt(encoded,'xX7b')

show_histogram([ord(x) for x in ''.join([x for x in encoded])])

print(input_text[0:57])
print(encoded[0:57])
print(decoded[0:57])