import secrets
import string
class Cipher:
    def __init__(self, key=None):
        if key is None:
            key = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(100))
        elif not key.islower() or not key.isalpha():
            raise ValueError("Key must consist of lowercase letters only.")
        self.key = key

    def encode(self, text):
        encoded = []
        for char in text:
            if char.isalpha():
                offset = string.ascii_lowercase.index(self.key[len(encoded) % len(self.key)])
                encoded_char = chr((ord(char) - ord('a') + offset) % 26 + ord('a'))
                encoded.append(encoded_char)
            else:
                encoded.append(char)
        return ''.join(encoded)

    def decode(self, text):
        decoded = []
        for char in text:
            if char.isalpha():
                offset = string.ascii_lowercase.index(self.key[len(decoded) % len(self.key)])
                decoded_char = chr((ord(char) - ord('a') - offset) % 26 + ord('a'))
                decoded.append(decoded_char)
            else:
                decoded.append(char)
        return ''.join(decoded)
