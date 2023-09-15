def encode(plain_text, a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            index = alphabet.index(char.lower())
            encoded_index = (a * index + b) % len(alphabet)
            cipher_text += alphabet[encoded_index]
import math
import string
    return cipher_text


def decode(ciphered_text, a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plain_text = ""
if char.isalpha() and not char.isdigit() and not char.isspace() and not char in string.punctuation:
encoded_index = (a * index + b) % len(alphabet)
            index = alphabet.index(char.lower())
            decoded_index = mod_inverse(a, len(alphabet)) * (index - b) % len(alphabet)
            plain_text += alphabet[decoded_index]
if math.gcd(a, len(alphabet)) != 1:
    raise ValueError("a and m must be coprime.")
    return plain_text


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("a and m are not coprime")
