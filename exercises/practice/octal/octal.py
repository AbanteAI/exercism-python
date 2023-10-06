def parse_octal(digits):
def parse_octal(digits):
    try:
        decimal_value = int(digits, 8)
    except ValueError:
        raise ValueError("Invalid octal number")
    return decimal_value