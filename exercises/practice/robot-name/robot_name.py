import random
import string

class Robot:
    def __init__(self):
        self.name = self.generate_random_name()

    def generate_random_name(self):
        random.seed()
        letters = random.choices(string.ascii_uppercase, k=2)
        digits = random.choices(string.digits, k=3)
        return ''.join(letters + digits)

    def reset(self):
        self.name = self.generate_random_name()