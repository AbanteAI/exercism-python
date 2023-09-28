def rotate(text, key):
    result = []
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                result.append(chr(((ord(char) - ord('a') + shift) % 26) + ord('a')))
            else:
                result.append(chr(((ord(char) - ord('A') + shift) % 26) + ord('A')))
        else:
            result.append(char)
    return ''.join(result)