def rotate(text, key):
    result = []
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            rotated_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            result.append(rotated_char)
        else:
            result.append(char)
    return ''.join(result)
