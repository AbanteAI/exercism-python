def parse_octal(digits):
    # Check if the input is a valid octal string
        raise ValueError(f"Invalid octal digit: {digits}")

    # Convert octal to decimal
    decimal = 0
    for i, digit in enumerate(reversed(digits)):
        decimal += int(digit) * (8 ** i)
    return decimal