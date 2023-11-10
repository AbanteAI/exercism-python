def encode(plain_text, a, b):
    if not are_coprime(a, 26):
        raise ValueError("a and m must be coprime.")

    encoded = []
    for char in plain_text.lower():
        if char.isalpha():
            index = ord(char) - ord('a')
            encoded_value = (a * index + b) % 26
            encoded.append(chr(encoded_value + ord('a')))
        elif char.isdigit():
            encoded.append(char)

    return ' '.join([''.join(encoded[i:i+5]) for i in range(0, len(encoded), 5)])

def decode(ciphered_text, a, b):
    if not are_coprime(a, 26):
        raise ValueError("a and m must be coprime.")

    decoded = []
    mmi = mod_inverse(a, 26)
    for char in ciphered_text:
        if char.isalpha():
            index = ord(char) - ord('a')
            decoded_value = (mmi * (index - b)) % 26
            decoded.append(chr(decoded_value + ord('a')))
        elif char.isdigit():
            decoded.append(char)

    return ''.join(decoded)

def are_coprime(a, b):
    while b:
        a, b = b, a % b
    return a == 1

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse found.")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a