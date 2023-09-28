def encode(plain_text, a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_text = ""
    for char in plain_text:
        if char.isalpha():
            index = alphabet.index(char.lower())
            encoded_index = (a * index + b) % len(alphabet)
            encoded_char = alphabet[encoded_index]
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text


def decode(ciphered_text, a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_text = ""
    try:
        a_inverse = pow(a, -1, len(alphabet))
    except ValueError:
        raise ValueError("a and m must be coprime.")
    for char in ciphered_text:
        if char.isalpha():
            index = alphabet.index(char.lower())
            decoded_index = (a_inverse * (index - b)) % len(alphabet)
            decoded_char = alphabet[decoded_index]
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text