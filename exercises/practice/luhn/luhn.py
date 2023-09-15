class Luhn:
    def __init__(self, card_num):
    def __init__(self, card_num):
        self.card_num = card_num.strip().replace(" ", "")
    
    def valid(self):
        if not self.card_num.isdigit():
            return False
        
        digits = [int(d) for d in self.card_num]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        
        return sum(digits) % 10 == 0
        pass
