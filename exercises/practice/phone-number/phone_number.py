class PhoneNumber:
    def __init__(self, number):
        self.number = ''.join(c for c in number if c.isdigit())
        if len(self.number) == 11 and self.number[0] == '1':
            self.number = self.number[1:]
        pass
    @property
    def area_code(self):
        return self.number[:3]
