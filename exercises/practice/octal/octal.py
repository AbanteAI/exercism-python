def parse_octal(digits):
    decimal = 0
    power = 0
    for digit in reversed(digits):
        if not digit.isdigit() or int(digit) >= 8:
            return 0
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal
    power = 0
    for digit in reversed(digits):
        if not digit.isdigit() or int(digit) >= 8:
            return 0
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal
    power = 0
    for digit in reversed(digits):
        if not digit.isdigit() or int(digit) >= 8:
            return 0
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal
