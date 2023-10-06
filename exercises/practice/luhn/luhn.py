class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if not self.card_num.isdigit() or len(self.card_num) <= 1:
            return False

        digits = [int(d) for d in self.card_num]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] = (digits[i] * 2) if (digits[i] * 2) <= 9 else (digits[i] * 2 - 9)

        return sum(digits) % 10 == 0
