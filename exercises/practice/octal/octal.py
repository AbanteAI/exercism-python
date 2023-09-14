def parse_octal(digits):
    if not digits.isdigit() or any(digit in "89" for digit in digits):
        raise ValueError("Invalid octal number")

    return int(digits, 8)