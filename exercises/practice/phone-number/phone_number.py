import re
import string
class PhoneNumber:
    def __init__(self, number):
        cleaned_number = re.sub(r'\D', '', number)
        if len(cleaned_number) == 11 and cleaned_number[0] == '1':
            cleaned_number = cleaned_number[1:]
        if len(cleaned_number) != 10:
            raise ValueError("Invalid number")
        if cleaned_number[0] in ['0', '1'] or cleaned_number[3] in ['0', '1']:
            raise ValueError("Invalid number")
        self.number = cleaned_number
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
