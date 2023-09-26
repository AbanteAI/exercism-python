import random
class Robot:
        self.name = self.generate_random_name()
    def generate_random_name(self):
        letters = [chr(random.randint(65, 90)) for _ in range(2)]  # Generate two random uppercase letters
        digits = [str(random.randint(0, 9)) for _ in range(3)]  # Generate three random digits
        return "".join(letters + digits)
