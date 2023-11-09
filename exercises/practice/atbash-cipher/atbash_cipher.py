def encode(plain_text):
    cipher = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba')
    encoded = plain_text.lower().translate(cipher)
    encoded = ''.join(char for char in encoded if char.isalnum())
    return ' '.join(encoded[i:i+5] for i in range(0, len(encoded), 5))


def decode(ciphered_text):
    cipher = str.maketrans('zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz')
    decoded = ciphered_text.lower().translate(cipher)
    return ''.join(char for char in decoded if char.isalnum())
