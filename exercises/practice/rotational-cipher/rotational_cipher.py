def rotate(text, key):
    rotated_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                ascii_offset = 65
            else:
                ascii_offset = 97
            rotated_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            rotated_text += rotated_char
        else:
            rotated_text += char
    return rotated_text