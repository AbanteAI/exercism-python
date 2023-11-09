import random
import string

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        else:
            self.key = key

    def encode(self, text):
        encoded_chars = []
        for i, char in enumerate(text):
            key_char = self.key[i % len(self.key)]
            encoded_char = chr(((ord(char) - ord('a')) + (ord(key_char) - ord('a'))) % 26 + ord('a'))
            encoded_chars.append(encoded_char)
        return ''.join(encoded_chars)

    def decode(self, text):
        decoded_chars = []
        for i, char in enumerate(text):
            key_char = self.key[i % len(self.key)]
            decoded_char = chr(((ord(char) - ord('a')) - (ord(key_char) - ord('a'))) % 26 + ord('a'))
            decoded_chars.append(decoded_char)
        return ''.join(decoded_chars)
