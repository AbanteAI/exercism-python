def encode(plain_text, a, b):
    if modular_multiplicative_inverse(a, 26) is None:
        raise ValueError("a and m must be coprime")
    
    plain_text = plain_text.lower()
    ciphered_text = ""

    for char in plain_text:
        if char.isalpha():
            i = ord(char) - ord('a')
            ciphered_char = chr(((a * i + b) % 26) + ord('a'))
        else:
            ciphered_char = char
        ciphered_text += ciphered_char
    
    return ciphered_text


def decode(ciphered_text, a, b):
    a_inv = modular_multiplicative_inverse(a, 26)
    
    if a_inv is None:
        raise ValueError("a and m must be coprime")
    
    plain_text = ""

    if char.isalpha():
        y = ord(char) - ord('a')
        plain_char = chr(((a_inv * (y - b)) % 26) + ord('a'))
    else:
        plain_char = char
    plain_text += plain_char
    
    return plain_text

def modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None