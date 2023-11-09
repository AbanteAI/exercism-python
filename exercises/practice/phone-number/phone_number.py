class PhoneNumber:
    def __init__(self, number):
        # Remove punctuation and spaces
        clean_number = ''.join(filter(str.isdigit, number))

        # Validate the number of digits
        if len(clean_number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(clean_number) > 11:
            raise ValueError("must not be greater than 11 digits")

        # Validate the country code if the number has 11 digits
        if len(clean_number) == 11:
            if clean_number[0] != '1':
                raise ValueError("11 digits must start with 1")
            clean_number = clean_number[1:]

        # Validate the area code
        if clean_number[0] == '0':
            raise ValueError("area code cannot start with zero")
        if clean_number[0] == '1':
            raise ValueError("area code cannot start with one")

        # Validate the exchange code
        if clean_number[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        if clean_number[3] == '1':
            raise ValueError("exchange code cannot start with one")

        self.number = clean_number
        self.area_code = self.number[:3]
