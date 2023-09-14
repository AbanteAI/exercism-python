from math import gcd
from math import gcd
import string
import string
def encode(plain_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    plain_text = plain_text.lower()
    plain_text = ''.join(c for c in plain_text if c.isalnum())
    ciphered_text = ''
    for c in plain_text:
        if c.isalpha():
            ciphered_text += chr(((a * (ord(c) - ord('a')) + b) % 26) + ord('a'))
        else:
            ciphered_text += c
    return ' '.join(ciphered_text[i:i + 5] for i in range(0, len(ciphered_text), 5))


def decode(ciphered_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    ciphered_text = ciphered_text.replace(' ', '')
    plain_text = ''
    a_inv = pow(a, -1, 26)
    for c in ciphered_text:
        if c.isalpha():
            plain_text += chr(((a_inv * (ord(c) - ord('a') - b)) % 26) + ord('a'))
        else:
            plain_text += c
    return plain_text
