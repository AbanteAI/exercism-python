class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False

        digits = [int(d) for d in self.card_num]
        for i in range(-2, -len(digits) - 1, -2):
            doubled = digits[i] * 2
            digits[i] = doubled - 9 if doubled > 9 else doubled

        return sum(digits) % 10 == 0
