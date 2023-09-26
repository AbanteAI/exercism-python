class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")
        self.valid_chars = all(ch.isdigit() for ch in self.card_num) and len(self.card_num) > 1
        pass

    def valid(self):
        if not self.valid_chars:
            return False

        digits = list(map(int, self.card_num))
        for i in range(len(digits) - 2, -1, -2):
            doubled = digits[i] * 2
            digits[i] = doubled if doubled <= 9 else doubled - 9

        return sum(digits) % 10 == 0
