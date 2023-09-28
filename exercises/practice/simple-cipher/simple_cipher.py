import string
import random

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        elif key.islower() and key.isalpha():
            self.key = key
        else:
            raise ValueError("Invalid key")
        else:
            raise ValueError("Invalid key")
        elif key.islower() and key.isalpha():
            self.key = key
        else:
            raise ValueError("Invalid key")

    def encode(self, text):
        encoded = []
        for i, char in enumerate(text):
            if char.islower():
                shift = string.ascii_lowercase.index(self.key[i % len(self.key)])
                encoded_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                encoded.append(encoded_char)
            elif char.isupper():
                shift = string.ascii_lowercase.index(self.key[i % len(self.key)])
                encoded_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                encoded.append(encoded_char)
        return ''.join(encoded)

    def decode(self, text):
        decoded = []
        for i, char in enumerate(text):
            if char.islower():
                shift = string.ascii_lowercase.index(self.key[i % len(self.key)])
                decoded_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                decoded.append(decoded_char)
            elif char.isupper():
                shift = string.ascii_lowercase.index(self.key[i % len(self.key)])
                decoded_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                decoded.append(decoded_char)
        return ''.join(decoded)
