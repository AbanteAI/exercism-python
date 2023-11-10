def encode(plain_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    atbash = {alphabet[i]: alphabet[-(i+1)] for i in range(len(alphabet))}
    encoded = ''.join(atbash.get(char, char) for char in plain_text.lower() if char.isalnum())
    return ' '.join(encoded[i:i+5] for i in range(0, len(encoded), 5))


def decode(ciphered_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    atbash = {alphabet[i]: alphabet[-(i+1)] for i in range(len(alphabet))}
    return ''.join(atbash.get(char, char) for char in ciphered_text.lower() if char.isalnum())
