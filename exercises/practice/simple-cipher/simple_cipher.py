import random
import string


class Cipher:
    def __init__(self, key=None):
        if key is not None:
            if not key.islower() or not key.isalpha():
                raise ValueError("Key must contain only lowercase letters")
            self.key = key
        else:
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))

    def encode(self, text):
        encoded = ""
        for i, char in enumerate(text):
            shift = ord(self.key[i % len(self.key)]) - ord("a")
            encoded += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        return encoded

    def decode(self, text):
        decoded = ""
        for i, char in enumerate(text):
            shift = ord(self.key[i % len(self.key)]) - ord("a")
            decoded += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        return decoded