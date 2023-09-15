def parse_octal(digits):
    decimal = 0
    try:
        for i, digit in enumerate(digits[::-1]):
            if not digit.isdigit() or int(digit) >= 8:
                raise ValueError
            decimal += int(digit) * (8 ** i)
    except ValueError:
        return 0
    return decimal
