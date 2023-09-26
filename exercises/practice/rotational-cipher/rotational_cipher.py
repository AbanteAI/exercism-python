def rotate(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result
