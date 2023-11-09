def parse_octal(digits):
    if not all(digit in '01234567' for digit in digits):
        raise ValueError("Invalid octal digit")
    decimal_value = 0
    for index, digit in enumerate(reversed(digits)):
        decimal_value += int(digit) * (8 ** index)
    return decimal_value
