def parse_octal(digits):
    if any(c not in "01234567" for c in digits):
        raise ValueError("Invalid octal input")

    decimal_number = 0
    for i, digit in enumerate(reversed(digits)):
        decimal_number += int(digit) * (8 ** i)

    return decimal_number