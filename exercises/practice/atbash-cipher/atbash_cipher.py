def encode(plain_text):
    plain_text = plain_text.lower()
    plain_alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_alphabet = plain_alphabet[::-1]
    translation_table = str.maketrans(plain_alphabet + "0123456789", cipher_alphabet + "0123456789")
    ciphered_text = plain_text.translate(translation_table)
    ciphered_text = ''.join(c for c in ciphered_text if c.isalnum())
    return ' '.join(ciphered_text[i:i+5] for i in range(0, len(ciphered_text), 5))


def decode(ciphered_text):
    plain_alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_alphabet = plain_alphabet[::-1]
    translation_table = str.maketrans(cipher_alphabet, plain_alphabet)
    plain_text = ciphered_text.translate(translation_table)
    return ''.join(c for c in plain_text if c.isalnum())
