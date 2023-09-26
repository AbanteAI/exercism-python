def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
from math import gcd
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
from math import gcd
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
from math import gcd
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
from math import gcd
from math import gcd
from math import gcd
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
from math import gcd
from math import gcd
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
from math import gcd
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def encode(plain_text, a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_text = ""
    
    # Remove spaces and punctuation characters
    plain_text = "".join(filter(str.isalnum, plain_text.lower()))
    
    # Check if a and m are coprime
    m = len(alphabet)
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime")
    
    for char in plain_text:
        if char.isdigit():
            encoded_text += char
        else:
            index = alphabet.index(char)
            encoded_index = (a * index + b) % m
            encoded_text += alphabet[encoded_index]
    
    # Group the encoded text in groups of 5 letters
    grouped_text = [encoded_text[i:i+5] for i in range(0, len(encoded_text), 5)]
    return " ".join(grouped_text)


def decode(ciphered_text, a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_text = ""
    
    # Remove spaces
    ciphered_text = ciphered_text.replace(" ", "")
    
    # Check if a and m are coprime
    m = len(alphabet)
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime")
    
    # Find the modular multiplicative inverse of a
    a_inverse = find_modular_multiplicative_inverse(a, m)
    
    for char in ciphered_text:
        if char.isdigit():
            decoded_text += char
        else:
            index = alphabet.index(char)
            decoded_index = (a_inverse * (index - b)) % m
            decoded_text += alphabet[decoded_index]
    
    return decoded_text
