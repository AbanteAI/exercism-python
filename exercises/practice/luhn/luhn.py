class Luhn:
    def __init__(self, card_num):
        pass

    def valid(self):
    def valid(self):
        if not self.card_num.isdigit() or len(self.card_num) <= 1:
            return False

        digits = [int(d) for d in self.card_num]
        doubled = [(2 * d - 9) if d > 4 else 2 * d for i, d in enumerate(digits[::-1])]

        return sum(doubled) % 10 == 0

