import string
import random
class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        else:
            self.key = key.lower()

    def encode(self, text):
        encoded = []
        for i, char in enumerate(text.lower()):
            shift = string.ascii_lowercase.index(self.key[i % len(self.key)])
            encoded.append(string.ascii_lowercase[(string.ascii_lowercase.index(char) + shift) % 26])
        return ''.join(encoded)

    def decode(self, text):
        decoded = []
        for i, char in enumerate(text.lower()):
            shift = string.ascii_lowercase.index(self.key[i % len(self.key)])
            decoded.append(string.ascii_lowercase[(string.ascii_lowercase.index(char) - shift) % 26])
        return ''.join(decoded)
