import string
import string

def is_coprime(a, m):
    while m:
        a, m = m, a % m
    return a == 1

def modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse exists for these values.")

def encode(plain_text, a, b):
    if not is_coprime(a, 26):
        raise ValueError("a and m must be coprime.")

    encoded = []
    for char in plain_text.lower():
        if char.isalpha():
            index = string.ascii_lowercase.index(char)
            encoded_char = (a * index + b) % 26
            encoded.append(string.ascii_lowercase[encoded_char])
        elif char.isdigit():
            encoded.append(char)

    return ' '.join([''.join(encoded[i:i+5]) for i in range(0, len(encoded), 5)])

def decode(ciphered_text, a, b):
    if not is_coprime(a, 26):
        raise ValueError("a and m must be coprime.")

    mmi = modular_multiplicative_inverse(a, 26)
    decoded = []
    for char in ciphered_text.replace(" ", "").lower():
        if char.isalpha():
            index = string.ascii_lowercase.index(char)
            decoded_char = (mmi * (index - b)) % 26
            decoded.append(string.ascii_lowercase[decoded_char])
        elif char.isdigit():
            decoded.append(char)

    return ''.join(decoded)


def decode(ciphered_text, a, b):
