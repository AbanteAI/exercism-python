def parse_octal(digits):
    if any(char not in "01234567" for char in digits):
        raise ValueError("Invalid octal input")

    decimal_value = 0
    for i, digit in enumerate(reversed(digits)):
        decimal_value += int(digit) * (8 ** i)
    return decimal_value