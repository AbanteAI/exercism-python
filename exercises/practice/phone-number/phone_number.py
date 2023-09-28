class PhoneNumber:
    def __init__(self, number):
        import re

        cleaned_number = re.sub(r'[^\d]', '', number)

        if not cleaned_number.isdigit():
            raise ValueError("letters not permitted")
        if re.search(r'[^\d\s\.\-\(\)]', number):
            raise ValueError("punctuations not permitted")
        if len(cleaned_number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(cleaned_number) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(cleaned_number) == 11:
            if cleaned_number[0] != '1':
                raise ValueError("11 digits must start with 1")
            cleaned_number = cleaned_number[1:]

        if cleaned_number[0] == '0':
            raise ValueError("area code cannot start with zero")
        elif cleaned_number[0] == '1':
            raise ValueError("area code cannot start with one")
        if cleaned_number[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        elif cleaned_number[3] == '1':
    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
            raise ValueError("exchange code cannot start with one")

        self.number = cleaned_number
    @property
    def area_code(self):
        return self.number[:3]