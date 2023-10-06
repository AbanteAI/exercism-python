import random
class Robot:
    def __init__(self):
        self.name = self.generate_unique_name()
    existing_names = set()

    def generate_unique_name(self):
        while True:
            new_name = self.generate_random_name()
            if new_name not in Robot.existing_names:
                Robot.existing_names.add(new_name)
                return new_name

    def generate_random_name(self):
        letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
        digits = ''.join(random.choices('0123456789', k=3))
        return letters + digits











    def reset(self):
        self.name = self.generate_unique_name()