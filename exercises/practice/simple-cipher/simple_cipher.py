import random
import string

class Cipher:
    def __init__(self, key=None):
        if key is None:
            key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        elif not key.islower() or not key.isalpha():
            raise ValueError("Key must consist of lowercase letters only.")
        self.key = key

    def encode(self, text):
        encoded = []
        for i, char in enumerate(text):
            if char.islower():
                offset = ord(self.key[i % len(self.key)]) - ord('a')
                encoded_char = chr((ord(char) - ord('a') + offset) % 26 + ord('a'))
                encoded.append(encoded_char)
            else:
                encoded.append(char)
        return ''.join(encoded)

    def decode(self, text):
        decoded = []
        for i, char in enumerate(text):
            if char.islower():
                offset = ord(self.key[i % len(self.key)]) - ord('a')
                decoded_char = chr((ord(char) - ord('a') - offset) % 26 + ord('a'))
                decoded.append(decoded_char)
            else:
                decoded.append(char)
        return ''.join(decoded)
