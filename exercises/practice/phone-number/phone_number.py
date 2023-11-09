import re

class PhoneNumber:

class PhoneNumber:
    def __init__(self, number):
        # Remove punctuation and country code if present
        clean_number = re.sub(r'\D', '', number)
        if clean_number.startswith('1'):
            clean_number = clean_number[1:]

        # Validate the length of the phone number
        if len(clean_number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(clean_number) > 10:
            raise ValueError("must not be greater than 10 digits")

        # Validate that the phone number does not contain letters
        if re.search(r'[a-zA-Z]', clean_number):
            raise ValueError("letters not permitted")

        # Validate the area code
        if clean_number[0] in '01':
            raise ValueError("area code cannot start with zero or one")

        # Validate the exchange code
        if clean_number[3] in '01':
            raise ValueError("exchange code cannot start with zero or one")

        self.number = clean_number
        self.area_code = clean_number[:3]
        self.exchange_code = clean_number[3:6]
        self.subscriber_number = clean_number[6:]
