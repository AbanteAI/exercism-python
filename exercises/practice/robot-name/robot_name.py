import random
import string

class Robot:
    all_names = set()

    def __init__(self):
        self.name = self._generate_unique_name()

    def reset(self):
        self.name = self._generate_unique_name()

    @classmethod
    def _generate_unique_name(cls):
        while True:
            name = cls._generate_random_name()
            if name not in cls.all_names:
                cls.all_names.add(name)
                return name

    @staticmethod
    def _generate_random_name():
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=3))
        return letters + numbers
