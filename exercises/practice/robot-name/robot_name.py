import random

class Robot:
    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
        random.seed()
        letters = [chr(random.randint(65, 90)) for _ in range(2)]
        digits = [str(random.randint(0, 9)) for _ in range(3)]
        return ''.join(letters + digits)

    def reset(self):
        self.name = self.generate_name()