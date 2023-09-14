def rotate(text, key):
    result = []
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result.append(chr(((ord(char) - offset + key) % 26) + offset))
        else:
            result.append(char)
    return ''.join(result)
