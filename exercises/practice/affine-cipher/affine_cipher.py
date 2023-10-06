import math
    if not coprime(a, 26):
def coprime(a, b):
    return math.gcd(a, b) == 1
        raise ValueError("a and m must be coprime.")
    encoded_text = ""
    for char in plain_text.lower():
        if char.isalpha():
            char_index = ord(char) - ord('a')
            encoded_char = chr(((a * char_index + b) % 26) + ord('a'))
            encoded_text += encoded_char
    return encoded_text


def decode(ciphered_text, a, b):
    if not coprime(a, 26):
        raise ValueError("a and m must be coprime.")
    decoded_text = ""
    a_inverse = find_inverse(a, 26)
    for char in ciphered_text.lower():
        if char.isalpha():
            char_index = ord(char) - ord('a')
        decoded_char = chr(((a_inverse * (char_index - b)) % 26) + ord('a'))
            decoded_text += decoded_char
    return decoded_text
