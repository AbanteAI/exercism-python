import random
import string
class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        else:
            self.key = key

    def encode(self, text):
        encoded = []
        for i, char in enumerate(text):
            shift = ord(self.key[i % len(self.key)]) - ord('a')
            encoded.append(chr(((ord(char) - ord('a') + shift) % 26) + ord('a')))
        return ''.join(encoded)

    def decode(self, text):
        decoded = []
        for i, char in enumerate(text):
            shift = ord(self.key[i % len(self.key)]) - ord('a')
            decoded.append(chr(((ord(char) - ord('a') - shift) % 26) + ord('a')))
        return ''.join(decoded)
