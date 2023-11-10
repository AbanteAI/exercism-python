class PhoneNumber:
    def __init__(self, number):
        # Remove punctuation and spaces
        clean_number = ''.join(filter(str.isdigit, number))

        # Validate the length of the number
        if len(clean_number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(clean_number) > 11:
            raise ValueError("must not be greater than 11 digits")

        # Validate country code if number is 11 digits
        if len(clean_number) == 11:
            if clean_number[0] != '1':
                raise ValueError("11 digits must start with 1")
            clean_number = clean_number[1:]

        # Validate area code
        if clean_number[0] in '01':
            raise ValueError("area code cannot start with zero or one")

        # Validate exchange code
        if clean_number[3] in '01':
            raise ValueError("exchange code cannot start with zero or one")

        # Assign cleaned and validated number to an instance variable
        self.number = clean_number
    clean_number = ''.join(filter(str.isdigit, number))

    # Validate the length of the number
    if len(clean_number) < 10:
        raise ValueError("must not be fewer than 10 digits")
    if len(clean_number) > 11:
        raise ValueError("must not be greater than 11 digits")

    # Validate country code if number is 11 digits
    if len(clean_number) == 11:
        if clean_number[0] != '1':
            raise ValueError("11 digits must start with 1")
        clean_number = clean_number[1:]

    # Validate area code
    if clean_number[0] in '01':
        raise ValueError("area code cannot start with zero or one")

    # Validate exchange code
    if clean_number[3] in '01':
        raise ValueError("exchange code cannot start with zero or one")

    # Assign cleaned and validated number to an instance variable
    self.number = clean_number
