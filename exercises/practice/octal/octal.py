def parse_octal(digits):
    decimal = 0
    for digit in digits:
        if not digit.isdigit() or int(digit) > 7:
            raise ValueError("Invalid octal digit")
        decimal = decimal * 8 + int(digit)
    return decimal
