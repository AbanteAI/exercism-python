class PhoneNumber:
    def __init__(self, number):
        # Clean up the phone number by removing punctuation and country code
        cleaned_number = ""
        for char in number:
            if char.isdigit():
                cleaned_number += char
        if len(cleaned_number) == 11 and cleaned_number[0] == "1":
            cleaned_number = cleaned_number[1:]
        self.number = cleaned_number

        # Check for invalid phone numbers and raise ValueError with appropriate messages
        if len(cleaned_number) < 10:
            raise ValueError("Phone number must not be fewer than 10 digits")
        if len(cleaned_number) > 11:
            raise ValueError("Phone number must not be greater than 11 digits")
        if len(cleaned_number) == 11 and cleaned_number[0] != "1":
            raise ValueError("11-digit phone number must start with 1")
        if cleaned_number[0] == "0":
            raise ValueError("Area code cannot start with zero")
        if cleaned_number[0] == "1":
            raise ValueError("Area code cannot start with one")
        if cleaned_number[3] == "0":
            raise ValueError("Exchange code cannot start with zero")
        if cleaned_number[3] == "1":
            raise ValueError("Exchange code cannot start with one")
        if not cleaned_number.isdigit():
            raise ValueError("Phone number cannot contain letters or punctuation")

    @property
    def area_code(self):
        return self.number[:3]
        cleaned_number = ""
        for char in number:
            if char.isdigit():
                cleaned_number += char
        if len(cleaned_number) == 11 and cleaned_number[0] == "1":
            cleaned_number = cleaned_number[1:]
        self.number = cleaned_number

        # Check for invalid phone numbers and raise ValueError with appropriate messages
        if len(cleaned_number) < 10:
            raise ValueError("Phone number must not be fewer than 10 digits")
        if len(cleaned_number) > 11:
            raise ValueError("Phone number must not be greater than 11 digits")
        if len(cleaned_number) == 11 and cleaned_number[0] != "1":
            raise ValueError("11-digit phone number must start with 1")
        if cleaned_number[0] == "0":
            raise ValueError("Area code cannot start with zero")
        if cleaned_number[0] == "1":
            raise ValueError("Area code cannot start with one")
        if cleaned_number[3] == "0":
            raise ValueError("Exchange code cannot start with zero")
        if cleaned_number[3] == "1":
            raise ValueError("Exchange code cannot start with one")
        if not cleaned_number.isdigit():
            raise ValueError("Phone number cannot contain letters or punctuation")
