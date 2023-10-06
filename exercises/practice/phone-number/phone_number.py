class PhoneNumber:
    def __init__(self, number):
        cleaned_number = ''.join(c for c in number if c.isdigit())
        if len(cleaned_number) == 11 and cleaned_number[0] != '1':
            raise ValueError("11 digits must start with 1")
        if len(cleaned_number) != 10:
            raise ValueError("must not be fewer than 10 digits")
        if cleaned_number[0] in ['0', '1']:
            raise ValueError("area code cannot start with zero")
        if cleaned_number[3] in ['0', '1']:
            raise ValueError("exchange code cannot start with zero")
        self.number = cleaned_number
