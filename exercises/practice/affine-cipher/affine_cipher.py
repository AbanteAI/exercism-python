import math
from string import ascii_lowercase

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_mod_inverse(a, m):
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime.")
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse found.")

def encode(plain_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    
    def encode_char(char):
        if char.isalpha():
            i = ascii_lowercase.index(char)
            return ascii_lowercase[(a * i + b) % 26]
        return char

    encoded_text = ''.join(encode_char(char) for char in plain_text.lower() if char.isalnum())
    return ' '.join(encoded_text[i:i+5] for i in range(0, len(encoded_text), 5))

def decode(ciphered_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    
    mod_inverse = find_mod_inverse(a, 26)
    
    def decode_char(char):
        if char.isalpha():
            y = ascii_lowercase.index(char)
            return ascii_lowercase[(mod_inverse * (y - b)) % 26]
        return char

    return ''.join(decode_char(char) for char in ciphered_text.replace(' ', '').lower())
