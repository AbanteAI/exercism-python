import string
import math
def encode(plain_text, a, b):
    if not are_coprime(a, 26):
        raise ValueError("a and m must be coprime.")
    plain_text = plain_text.lower().replace(" ", "")
    result = []
    for char in plain_text:
        if char.isalpha():
            result.append(string.ascii_lowercase[(a * (string.ascii_lowercase.index(char)) + b) % 26])
        elif char.isdigit():
            result.append(char)
    return ''.join(result)


def decode(ciphered_text, a, b):
    if not are_coprime(a, 26):
        raise ValueError("a and m must be coprime.")
    ciphered_text = ciphered_text.lower().replace(" ", "")
    result = []
    a_inv = mod_inverse(a, 26)
    for char in ciphered_text:
        if char.isalpha():
            result.append(string.ascii_lowercase[(a_inv * (string.ascii_lowercase.index(char) - b)) % 26])
        elif char.isdigit():
            result.append(char)
    return ''.join(result)
def are_coprime(a, b):
    return math.gcd(a, b) == 1

def mod_inverse(a, m):
    if math.gcd(a, m) != 1:
        raise ValueError("a and m must be coprime.")
    return pow(a, -1, m)
