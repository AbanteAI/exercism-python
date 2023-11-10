class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.strip().replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False

def double_and_subtract(n):
    return n if n < 5 else n * 2 - 9

def valid(self):
    if len(self.card_num) <= 1 or not self.card_num.isdigit():
        return False

    digits = [int(d) for d in reversed(self.card_num)]
    checksum = sum(double_and_subtract(d) if (i + 1) % 2 == 0 else d for i, d in enumerate(digits))

    return checksum % 10 == 0
