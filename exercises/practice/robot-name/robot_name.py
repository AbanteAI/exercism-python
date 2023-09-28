import random
import string
_used_names = set()
class Robot:
    def __init__(self):
        self.name = self._generate_random_name()
    def _generate_random_name(self):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            digits = ''.join(random.choices(string.digits, k=3))
            name = letters + digits
            if name not in _used_names:
                _used_names.add(name)
                return name

    def reset(self):
        self.name = self._generate_random_name()