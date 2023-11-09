import re

class PhoneNumber:

class PhoneNumber:
    def __init__(self, number):
        # Remove punctuation and country code
        cleaned_number = re.sub(r'\D', '', number)
        if cleaned_number.startswith('1'):
            cleaned_number = cleaned_number[1:]

        # Validate the phone number
        if len(cleaned_number) != 10:
            raise ValueError("number must be 10 digits")
        if not re.match(r'^[2-9]\d{2}[2-9]\d{6}$', cleaned_number):
            raise ValueError("number has invalid format")

        # Assign attributes
        self.area_code = cleaned_number[:3]
        self.exchange_code = cleaned_number[3:6]
        self.subscriber_number = cleaned_number[6:]
        self.number = cleaned_number
