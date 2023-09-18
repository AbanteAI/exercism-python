import random
import string
class Robot:
    existing_names = set()
    def generate_name(self):
        while True:
            name = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=3))
            if name not in Robot.existing_names:
                Robot.existing_names.add(name)
                return name
    def __init__(self):
        self.name = self.generate_name()
    def reset(self):
        Robot.existing_names.remove(self.name)
        self.name = self.generate_name()