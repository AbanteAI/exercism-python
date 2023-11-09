def rotate(text, key):
    result = []
    for char in text:
        if char.isalpha():
            shift = key % 26
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)
