def rotate(text, key):
    def shift_char(c):
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            return chr((ord(c) - base + key) % 26 + base)
        else:
            return c

    return ''.join(shift_char(c) for c in text)
