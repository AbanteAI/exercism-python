class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False

        reversed_digits = [int(digit) for digit in reversed(self.card_num)]
        for index in range(1, len(reversed_digits), 2):
            reversed_digits[index] *= 2
            if reversed_digits[index] > 9:
                reversed_digits[index] -= 9

        total_sum = sum(reversed_digits)
        return total_sum % 10 == 0
