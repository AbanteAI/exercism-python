class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")
    def _double_second_digits(self):
        doubled = []
        for i, digit in enumerate(reversed(self.card_num)):
            if i % 2 != 0:
                doubled_digit = int(digit) * 2
                doubled.append(doubled_digit - 9 if doubled_digit > 9 else doubled_digit)
            else:
                doubled.append(int(digit))
        return doubled

    def _sum_digits(self, doubled):
        return sum(doubled)
    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False
        doubled = self._double_second_digits()
        total_sum = self._sum_digits(doubled)
        return total_sum % 10 == 0
