import random
class Robot:
    def __init__(self):
used_names = set()
    def __init__(self):
        self.name = self.generate_name()
    def generate_name(self):
        while True:
            name = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(2))
            name += ''.join(random.choice('0123456789') for _ in range(3))
            if name not in used_names:
                used_names.add(name)
                return name





    def reset(self):
        self.name = self.generate_name()