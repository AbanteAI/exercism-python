def encode(plain_text):
    plain_text = plain_text.lower()
    ciphered_text = ""
    for char in plain_text:
        if char.isalnum():
            if char.isalpha():
                char = chr(25 - ord(char) + 2 * ord('a'))
            ciphered_text += char
    return ' '.join(ciphered_text[i:i+5] for i in range(0, len(ciphered_text), 5))


def decode(ciphered_text):
    decoded_text = ""
    for char in ciphered_text:
        if char.isalnum():
            if char.isalpha():
                char = chr(25 - ord(char) + 2 * ord('a'))
            decoded_text += char
    return decoded_text
