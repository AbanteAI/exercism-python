class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_number(number)

    def clean_number(self, number):
        cleaned_number = ''.join(c for c in number if c.isdigit())
        if len(cleaned_number) == 11 and cleaned_number[0] == '1':
            cleaned_number = cleaned_number[1:]
        if len(cleaned_number) != 10 or cleaned_number[0] in ['0', '1'] or cleaned_number[3] in ['0', '1']:
            raise ValueError("Invalid phone number")
        return cleaned_number