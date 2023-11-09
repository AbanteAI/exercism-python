import random
import string
class Robot:
    def __init__(self):
        self._name = None
        self._used_names = set()

    def _generate_name(self):
        while True:
            name = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=3))
            if name not in self._used_names:
                self._used_names.add(name)
                return name

    @property
    def name(self):
        if self._name is None:
            self._name = self._generate_name()
        return self._name

    def reset(self):
        self._name = None
