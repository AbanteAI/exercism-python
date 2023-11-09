import string
from math import gcd

def encode(plain_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    
    def affine_encrypt(char):
        if char.isalpha():
            y = (a * (ord(char) - ord('a')) + b) % 26
            return chr(y + ord('a'))
        return char
    
    sanitized_text = ''.join(filter(lambda c: c.isalpha() or c.isdigit(), plain_text.lower()))
    ciphered_text = ''.join(affine_encrypt(char) for char in sanitized_text)
    return ' '.join(ciphered_text[i:i+5] for i in range(0, len(ciphered_text), 5))

def decode(ciphered_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    
    def modular_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        raise ValueError("Modular inverse does not exist.")
    
    def affine_decrypt(char):
        if char.isalpha():
            x = modular_inverse(a, 26) * (ord(char) - ord('a') - b) % 26
            return chr(x + ord('a'))
        return char
    
    sanitized_text = ''.join(filter(lambda c: c.isalpha() or c.isdigit(), ciphered_text.lower()))
    plaintext = ''.join(affine_decrypt(char) for char in sanitized_text)
    return plaintext