def rotate(text, key):
    def shift_char(c):
        if c.isalpha():
            ascii_offset = ord('a') if c.islower() else ord('A')
            return chr((ord(c) - ascii_offset + key) % 26 + ascii_offset)
        else:
            return c

    return ''.join(shift_char(c) for c in text)
