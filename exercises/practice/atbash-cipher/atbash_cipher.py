def encode(plain_text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    encoded_text = ""

    for char in plain_text.lower():
        if char.isalpha():
            encoded_text += cipher[alphabet.index(char)]
        elif char.isdigit():
            encoded_text += char

    return " ".join([encoded_text[i:i + 5] for i in range(0, len(encoded_text), 5)])


def decode(ciphered_text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    decoded_text = ""

    for char in ciphered_text.lower():
        if char.isalpha():
            decoded_text += alphabet[cipher.index(char)]
        elif char.isdigit():
            decoded_text += char

    return decoded_text
