class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(chr(random.randint(ord('a'), ord('z'))) for _ in range(100))
        else:
            self.key = key

    def encode(self, text):
        encoded = []
        for i, char in enumerate(text):
            key_char = self.key[i % len(self.key)]
            encoded_char = chr(((ord(char) - ord('a')) + (ord(key_char) - ord('a'))) % 26 + ord('a'))
            encoded.append(encoded_char)
        return ''.join(encoded)

    def decode(self, text):
        decoded = []
        for i, char in enumerate(text):
            key_char = self.key[i % len(self.key)]
            decoded_char = chr(((ord(char) - ord('a')) - (ord(key_char) - ord('a'))) % 26 + ord('a'))
            decoded.append(decoded_char)
        return ''.join(decoded)
