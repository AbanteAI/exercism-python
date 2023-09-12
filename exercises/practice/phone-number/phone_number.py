class PhoneNumber:
    def __init__(self, number):
        pass
    def __clean_number(self, number):
        return ''.join([c for c in number if c.isdigit()])

    def __validate_number(self, number):
        if len(number) == 11 and number.startswith('1'):
            number = number[1:]
        if len(number) != 10 or number[0] in '01' or number[3] in '01':
            raise ValueError("Invalid phone number")
        return number

    def __init__(self, number):
        self.number = self.__validate_number(self.__clean_number(number))

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
