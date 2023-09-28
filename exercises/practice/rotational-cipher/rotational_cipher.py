def rotate(text, key):
    ciphertext = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            ciphertext += chr(shifted)
        else:
            ciphertext += char
    return ciphertext
