class Luhn:
    def __init__(self, card_num):
    def sum_digits(self):
        digits = [int(digit) for digit in self.card_num]
        for i in range(len(digits) - 2, -1, -2):
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            digits[i] = doubled
        return sum(digits)
    def sum_digits(self):
        digits = [int(digit) for digit in self.card_num]
        for i in range(len(digits) - 2, -1, -2):
        return self.sum_digits() % 10 == 0
            if doubled > 9:
                doubled -= 9
            digits[i] = doubled
        return sum(digits)
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        return self.sum_digits() % 10 == 0
