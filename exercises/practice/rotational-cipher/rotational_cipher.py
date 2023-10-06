def rotate(text, key):
    result = []
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result.append(chr(((ord(char) - shift + key) % 26) + shift))
        else:
            result.append(char)
    return ''.join(result)
