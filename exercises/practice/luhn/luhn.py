class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        num = self.card_num.replace(' ', '')
        if not num.isdigit() or len(num) <= 1:
            return False

        total = 0
        for i, digit in enumerate(reversed(num)):
            n = int(digit)
            if i % 2 != 0:
                n *= 2
                if n > 9:
                    n -= 9
            total += n

        return total % 10 == 0