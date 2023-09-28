def encode(plain_text, a, b):
    pass
import string

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime.")
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encode(plain_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    plain_text = plain_text.lower()
    alphabet = string.ascii_lowercase
    ciphered_text = ""
    for char in plain_text:
        if char.isalpha():
            i = alphabet.index(char)
            ciphered_text += alphabet[(a * i + b) % 26]
        elif char.isdigit():
            ciphered_text += char
    return ' '.join(ciphered_text[i:i+5] for i in range(0, len(ciphered_text), 5))

def decode(ciphered_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    ciphered_text = ciphered_text.replace(' ', '').lower()
    alphabet = string.ascii_lowercase
    a_inv = mod_inverse(a, 26)
    plain_text = ""
    for char in ciphered_text:
        if char.isalpha():
            i = alphabet.index(char)
            plain_text += alphabet[(a_inv * ((i - b) % 26)) % 26]
        elif char.isdigit():
            plain_text += char
    return plain_text


def decode(ciphered_text, a, b):
    pass
