import re
class PhoneNumber:
    def __init__(self, number):
        cleaned_number = re.sub(r"[^0-9]", "", number)
        if len(cleaned_number) == 11 and cleaned_number[0] == "1":
            cleaned_number = cleaned_number[1:]
        if (
            len(cleaned_number) != 10
            or int(cleaned_number[0]) < 2
            or int(cleaned_number[3]) < 2
        ):
            raise ValueError("punctuations not permitted")
        self.number = cleaned_number

    def __str__(self):
        return self.number
    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"