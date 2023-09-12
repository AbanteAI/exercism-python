def parse_octal(digits):
    if not digits.isdigit() or any(char in "89" for char in digits):
        raise ValueError("Invalid octal number")
    return int(digits, 8)