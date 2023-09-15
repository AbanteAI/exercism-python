class Cipher:
    def __init__(self, key=None):
        self.key = key if key else self.generate_random_key()

    def generate_random_key(self):
        import random
        import string

        return ''.join(random.choice(string.ascii_lowercase) for _ in range(100))

    def encode(self, text):
class Cipher:
    def __init__(self, key=None):
        self.key = key if key else self.generate_random_key()

    def generate_random_key(self):
        import random
        import string

        return ''.join(random.choice(string.ascii_lowercase) for _ in range(100))

    def encode(self, text):
        encoded_text = ""
        for char in text:
            if char.isalpha():
                encoded_char = chr((ord(char.lower()) - ord('a') + int(self.key)) % 26 + ord('a'))
                encoded_text += encoded_char
            else:
                encoded_text += char
        return encoded_text

    def decode(self, text):
        decoded_text = ""
        for char in text:
            if char.isalpha():
                decoded_char = chr((ord(char.lower()) - ord('a') - int(self.key)) % 26 + ord('a'))
                decoded_text += decoded_char
            else:
                decoded_text += char
        return decoded_text