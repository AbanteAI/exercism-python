def parse_octal(digits):
    if not all(digit.isdigit() and int(digit) < 8 for digit in digits):
        raise ValueError("Invalid octal input")
    for i, digit in enumerate(reversed(digits)):
        if not digit.isdigit() or int(digit) > 7:
            return 0
        decimal += int(digit) * (8 ** i)
    return decimal