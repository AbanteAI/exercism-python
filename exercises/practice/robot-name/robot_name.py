import random
import string
class Robot:
    def __init__(self):
        pass
    def generate_name(self):
        letters = random.choices(string.ascii_uppercase, k=2)
        numbers = random.choices(string.digits, k=3)
        return ''.join(letters + numbers)

    @property
    def name(self):
        if not hasattr(self, "_name"):
            self._name = self.generate_name()
        return self._name

    def reset(self):
        delattr(self, "_name")