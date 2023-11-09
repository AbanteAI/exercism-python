import re

class PhoneNumber:

class PhoneNumber:
    def __init__(self, number):
        # Remove all non-digit characters
        cleaned_number = re.sub(r'\D', '', number)

        # Validate the cleaned number
        if len(cleaned_number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(cleaned_number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(cleaned_number) == 11:
            if cleaned_number[0] != '1':
                raise ValueError("11 digits must start with 1")
            cleaned_number = cleaned_number[1:]  # Strip country code

        # Validate area code and exchange code
        if cleaned_number[0] in '01':
            raise ValueError("area code cannot start with zero or one")
        if cleaned_number[3] in '01':
            raise ValueError("exchange code cannot start with zero or one")

        # Store the validated phone number
        self.number = cleaned_number
