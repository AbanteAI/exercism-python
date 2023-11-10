def rotate(text, key):
    def shift_char(c):
        if c.isalpha():
            start = ord('a') if c.islower() else ord('A')
            return chr(start + (ord(c) - start + key) % 26)
        return c

    return ''.join(shift_char(c) for c in text)