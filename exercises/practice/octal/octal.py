def parse_octal(digits):
    if not digits.isdigit() or any(char in "89" for char in digits):
        raise ValueError("Invalid octal number")

    decimal_number = 0
    for i, digit in enumerate(reversed(digits)):
        decimal_number += int(digit) * (8 ** i)

    return decimal_number

    decimal_number = 0
    for i, digit in enumerate(reversed(digits)):
        decimal_number += int(digit) * (8 ** i)

    return decimal_number