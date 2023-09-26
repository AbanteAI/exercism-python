def parse_octal(digits):
    decimal = 0
    for i, digit in enumerate(reversed(digits)):
        if not digit.isdigit() or int(digit) >= 8:
            return 0
        decimal += int(digit) * (8 ** i)
    return decimal
    for i, digit in enumerate(reversed(digits)):
        if not digit.isdigit() or int(digit) >= 8:
            return 0
        decimal += int(digit) * (8 ** i)
    return decimal
