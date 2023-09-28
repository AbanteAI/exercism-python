def encode(plain_text):
    encoded_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                encoded_char = chr(ord('Z') - (ord(char) - ord('A')))
            else:
                encoded_char = chr(ord('z') - (ord(char) - ord('a')))
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text

def decode(ciphered_text):
    decoded_text = ""
    for char in ciphered_text:
        if char.isalpha():
            if char.isupper():
                decoded_char = chr(ord('Z') - (ord(char) - ord('A')))
            else:
                decoded_char = chr(ord('z') - (ord(char) - ord('a')))
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text
    for char in ciphered_text:
        if char.isalpha():
            if char.isupper():
                decoded_char = chr(ord('Z') - (ord(char) - ord('A')))
            else:
                decoded_char = chr(ord('z') - (ord(char) - ord('a')))
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text
