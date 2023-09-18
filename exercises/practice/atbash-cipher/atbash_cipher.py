def encode(plain_text):
    plain_text = plain_text.lower()
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    translation = str.maketrans(plain, cipher)
    encoded_text = ''.join(c if c.isdigit() else c.translate(translation) for c in plain_text if c.isalnum())
    return ' '.join(encoded_text[i:i+5] for i in range(0, len(encoded_text), 5))


def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(" ", "")
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    translation = str.maketrans(cipher, plain)
    return ciphered_text.translate(translation)
