import random
import string
class Robot:
    existing_names = set()
    def __init__(self):
        self.name = self.generate_name()
    def generate_name(self, seed=None):
        if seed is not None:
            random.seed(seed)
        name = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=3))
        while name in Robot.existing_names:
            name = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=3))
        Robot.existing_names.add(name)
        return name
        return name

    def reset(self):
        Robot.existing_names.remove(self.name)
        self.name = self.generate_name(seed=random.random())