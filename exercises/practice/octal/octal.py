def parse_octal(digits):
    # Check for invalid input
        raise ValueError("Invalid octal digit")

    # Reverse the digits for easier processing
    reversed_digits = digits[::-1]

    # Convert octal to decimal
    decimal_value = 0
    for index, digit in enumerate(reversed_digits):
        decimal_value += int(digit) * (8 ** index)

    return decimal_value