def encode(plain_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    atbash = {char: alphabet[::-1][i] for i, char in enumerate(alphabet)}
    encoded = ''.join(atbash.get(char, char) for char in plain_text.lower() if char.isalnum())
    return ' '.join(encoded[i:i+5] for i in range(0, len(encoded), 5))


def decode(ciphered_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    atbash = {alphabet[::-1][i]: char for i, char in enumerate(alphabet)}
    return ''.join(atbash.get(char, char) for char in ciphered_text.lower() if char.isalnum())
