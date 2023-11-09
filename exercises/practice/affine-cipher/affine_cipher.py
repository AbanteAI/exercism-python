def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_modular_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse found.")

def encode(plain_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    
    encoded = []
    for char in plain_text.lower():
        if char.isalpha():
            i = ord(char) - ord('a')
            encoded_char = chr(((a * i + b) % 26) + ord('a'))
            encoded.append(encoded_char)
        elif char.isdigit():
            encoded.append(char)
    
    return ' '.join([''.join(encoded[i:i+5]) for i in range(0, len(encoded), 5)])

def decode(ciphered_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    
    a_inverse = find_modular_inverse(a, 26)
    decoded = []
    for char in ciphered_text:
        if char.isalpha():
            y = ord(char) - ord('a')
            decoded_char = chr((a_inverse * (y - b) % 26) + ord('a'))
            decoded.append(decoded_char)
        elif char.isdigit():
            decoded.append(char)
    
    return ''.join(decoded)
