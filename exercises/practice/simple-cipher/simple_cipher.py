import random
import string

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        else:
            self.key = key.lower()

    def encode(self, text):
        encoded_text = []
        for i, char in enumerate(text.lower()):
            if char.isalpha():
                shift = ord(self.key[i % len(self.key)]) - ord('a')
                encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                encoded_text.append(encoded_char)
            else:
                encoded_text.append(char)
        return ''.join(encoded_text)

    def decode(self, text):
        decoded_text = []
        for i, char in enumerate(text.lower()):
            if char.isalpha():
                shift = ord(self.key[i % len(self.key)]) - ord('a')
                decoded_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                decoded_text.append(decoded_char)
            else:
                decoded_text.append(char)
        return ''.join(decoded_text)
