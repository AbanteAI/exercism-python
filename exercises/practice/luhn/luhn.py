class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False

        digits = [int(d) for d in self.card_num]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] = digits[i] * 2
            if digits[i] > 9:
                digits[i] -= 9

        total_sum = sum(digits)
        return total_sum % 10 == 0
