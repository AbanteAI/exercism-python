def find_modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("a and m must be coprime.")
    for char in plain_text:
        if char.isalpha():
            char = char.lower()
            index = ord(char) - ord('a')
            encrypted_index = (a * index + b) % 26
            encrypted_char = chr(encrypted_index + ord('a'))
            encoded_text += encrypted_char
        else:
            encoded_text += char
    return ' '.join([encoded_text[i:i+5] for i in range(0, len(encoded_text), 5)])


def decode(ciphered_text, a, b):
    decoded_text = ""
    a_inv = find_modular_multiplicative_inverse(a, 26)
    for char in ciphered_text:
        if char.isalpha():
            char = char.lower()
            index = ord(char) - ord('a')
            decrypted_index = (a_inv * (index - b)) % 26
            decrypted_char = chr(decrypted_index + ord('a'))
            decoded_text += decrypted_char
        else:
            decoded_text += char
    return decoded_text
