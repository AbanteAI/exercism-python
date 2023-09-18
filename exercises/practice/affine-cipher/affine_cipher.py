import string

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_coprime(a, m):
    return gcd(a, m) == 1

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encode(plain_text, a, b):
    if not is_coprime(a, 26):
        raise ValueError("a and m must be coprime.")

    plain_text = plain_text.lower()
    result = []
    for char in plain_text:
        if char.isalpha():
            i = string.ascii_lowercase.index(char)
            result.append(string.ascii_lowercase[(a * i + b) % 26])
        elif char.isdigit():
            result.append(char)

    return ' '.join([''.join(result[i:i+5]) for i in range(0, len(result), 5)])

def decode(ciphered_text, a, b):
    if not is_coprime(a, 26):
        raise ValueError("a and 26 must be coprime")

    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Modular inverse does not exist")

    ciphered_text = ciphered_text.replace(' ', '')
    for char in ciphered_text:
        if char.isalpha():
            y = string.ascii_lowercase.index(char)
            result.append(string.ascii_lowercase[(a_inv * (y - b)) % 26])
        elif char.isdigit():
            result.append(char)

    return ' '.join([''.join(result[i:i+5]) for i in range(0, len(result), 5)])