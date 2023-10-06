from math import gcd
def are_coprime(a, m):
    return gcd(a, m) == 1

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("No modular multiplicative inverse exists.")

def encode(plain_text, a, b):
    if not are_coprime(a, 26):
        raise ValueError("a and m must be coprime.")
    plain_text = plain_text.lower()
    ciphered_text = ""
    for char in plain_text:
        if char.isalpha():
            i = ord(char) - ord('a')
            ciphered_text += chr(((a * i + b) % 26) + ord('a'))
        else:
            continue
    return ' '.join([ciphered_text[i:i + 5] for i in range(0, len(ciphered_text), 5)])

def decode(ciphered_text, a, b):
    if not are_coprime(a, 26):
        raise ValueError("a and m must be coprime.")
    ciphered_text = ciphered_text.replace(' ', '').lower()
    plain_text = ""
    a_inverse = mod_inverse(a, 26)
    for char in ciphered_text:
        if char.isalpha():
            i = ord(char) - ord('a')
            plain_text += chr(((a_inverse * (i - b)) % 26) + ord('a'))
        elif char.isdigit():
            plain_text += char
    return plain_text


def decode(ciphered_text, a, b):
