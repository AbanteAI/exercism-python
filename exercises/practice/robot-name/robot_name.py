import random
import string
class Robot:
    def __init__(self):
        self.name = self._generate_unique_name()
        Robot._assigned_names.add(self.name)

    _assigned_names = set()

    def _generate_unique_name(self):
        while True:
            name = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=3))
            if name not in Robot._assigned_names:
                return name

    def reset(self):
        old_name = self.name
        self._assigned_names.remove(self.name)
        while True:
            self.name = self._generate_unique_name()
            if self.name != old_name:
                break
        Robot._assigned_names.add(self.name)
