class PhoneNumber:
    def __init__(self, number):
        import re

        # Remove all non-digit characters
        cleaned_number = re.sub(r'\D', '', number)

        # Check for valid length
        if len(cleaned_number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(cleaned_number) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(cleaned_number) == 11:
            if cleaned_number[0] != '1':
                raise ValueError("11 digits must start with 1")
            else:
                cleaned_number = cleaned_number[1:]

        # Check for valid area code and exchange code
        if cleaned_number[0] in ('0', '1'):
            raise ValueError("area code cannot start with zero or one")
        if cleaned_number[3] in ('0', '1'):
            raise ValueError("exchange code cannot start with zero or one")

        self.number = cleaned_number