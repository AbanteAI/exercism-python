def encode(plain_text):
    plain_text = plain_text.lower()
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            cipher_char = chr(ord('a') + (ord('z') - ord(char)))
            cipher_text += cipher_char
        elif char.isdigit():
            cipher_text += char
    return " ".join([cipher_text[i:i+5] for i in range(0, len(cipher_text), 5)])
    pass


def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(" ", "")
    plain_text = ""
    for char in ciphered_text:
        if char.isalpha():
            plain_char = chr(ord('a') + (ord('z') - ord(char)))
            plain_text += plain_char
        elif char.isdigit():
            plain_text += char
    return plain_text
    pass
