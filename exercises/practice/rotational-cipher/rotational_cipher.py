def rotate(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            rotated_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            result += rotated_char
        else:
            result += char
    return result