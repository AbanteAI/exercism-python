def encode(plain_text):
    cipher_text = []
    for char in plain_text:
        if char.isalpha():
            char = chr(ord('z') - (ord(char.lower()) - ord('a')))
        cipher_text.append(char)
    return ''.join(cipher_text)


def decode(ciphered_text):
    return encode(ciphered_text)
