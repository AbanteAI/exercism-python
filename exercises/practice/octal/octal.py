def parse_octal(digits):
    decimal = 0
    for digit in digits:
        if not digit.isdigit() or int(digit) >= 8:
            raise ValueError("Invalid octal digit: {}".format(digit))

        decimal = decimal * 8 + int(digit)
    return decimal
