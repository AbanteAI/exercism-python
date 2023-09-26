def rotate(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char
    return result