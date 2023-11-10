import random
import string

class Robot:
    _used_names = set()

    def __init__(self):
        self.name = self._generate_unique_name()

    def reset(self):
        self.name = self._generate_unique_name()

    def _generate_unique_name(self):
        while True:
            name = self._generate_random_name()
            if name not in Robot._used_names:
                Robot._used_names.add(name)
                return name

    def _generate_random_name(self):
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=3))
        return letters + numbers
