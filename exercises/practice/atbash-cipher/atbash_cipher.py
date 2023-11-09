def encode(plain_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    atbash = {alphabet[i]: alphabet[-(i+1)] for i in range(len(alphabet))}
    ciphered_text = []

    for char in plain_text.lower():
        if char.isalpha():
            ciphered_text.append(atbash[char])
        elif char.isdigit():
            ciphered_text.append(char)

    # Group the ciphered text into groups of 5 characters
    return ' '.join([''.join(ciphered_text[i:i+5]) for i in range(0, len(ciphered_text), 5)])


def decode(ciphered_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    atbash = {alphabet[-(i+1)]: alphabet[i] for i in range(len(alphabet))}
    plain_text = []

    for char in ciphered_text.lower():
        if char.isalpha():
            plain_text.append(atbash[char])
        elif char.isdigit():
            plain_text.append(char)

    return ''.join(plain_text)
