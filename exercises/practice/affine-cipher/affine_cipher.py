import math
def encode(plain_text, a, b):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_text = ''
    plain_text = plain_text.lower().replace(' ', '').replace(',', '').replace('.', '')

    if math.gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")

    for char in plain_text:
        if char.isalpha():
            index = alphabet.index(char)
            encoded_index = (a * index + b) % 26
            encoded_text += alphabet[encoded_index]
        else:
            encoded_text += char

    return ' '.join([encoded_text[i:i+5] for i in range(0, len(encoded_text), 5)])


def decode(ciphered_text, a, b):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded_text = ''

    if math.gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")

    for char in ciphered_text:
        if char.isalpha():
            index = alphabet.index(char)
            decoded_index = (modinv(a, 26) * (index - b)) % 26
            decoded_text += alphabet[decoded_index]
        else:
            decoded_text += char

    return decoded_text
