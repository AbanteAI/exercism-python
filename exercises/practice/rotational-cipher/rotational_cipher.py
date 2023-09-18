def rotate(text, key):
    return ''.join(shift_char(char, key) for char in text)

def shift_char(char, key):
    if 'a' <= char <= 'z':
        offset = ord('a')
        return chr(((ord(char) - offset + key) % 26) + offset)
    elif 'A' <= char <= 'Z':
        offset = ord('A')
        return chr(((ord(char) - offset + key) % 26) + offset)
    else:
        return char