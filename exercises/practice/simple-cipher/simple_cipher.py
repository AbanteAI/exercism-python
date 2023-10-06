class Cipher:
    class Cipher:
        def __init__(self, key=None):
            if key is None:
                key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
            self.key = key

        def encode(self, text):
            encoded = ''
            for i, char in enumerate(text):
                shift = ord(self.key[i % len(self.key)]) - ord('a')
                encoded += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            return encoded

        def decode(self, text):
            decoded = ''
            for i, char in enumerate(text):
                shift = ord(self.key[i % len(self.key)]) - ord('a')
                decoded += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            return decoded