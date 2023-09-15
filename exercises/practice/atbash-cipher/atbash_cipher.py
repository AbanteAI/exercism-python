def encode(plain_text):
    ciphered_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                ciphered_text += chr(155 - ord(char))
            else:
                ciphered_text += chr(219 - ord(char))
        else:
            ciphered_text += char
    return ciphered_text


def decode(ciphered_text):
    plain_text = ""
    for char in ciphered_text:
        if char.isalpha():
            if char.isupper():
                plain_text += chr(155 - ord(char))
            else:
                plain_text += chr(219 - ord(char))
        else:
            plain_text += char
    return plain_text
    return ciphered_text


def decode(ciphered_text):
    plain_text = ""
    for char in ciphered_text:
        if char.isalpha():
            if char.isupper():
                plain_text += chr(155 - ord(char))
            else:
                plain_text += chr(219 - ord(char))
        else:
            plain_text += char
    return plain_text