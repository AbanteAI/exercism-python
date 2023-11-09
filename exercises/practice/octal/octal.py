def parse_octal(digits):
    if not digits or any(c not in '01234567' for c in digits):
        raise ValueError("Invalid octal digit")
    decimal = 0
    for digit in digits:
        decimal = decimal * 8 + int(digit)
    return decimal