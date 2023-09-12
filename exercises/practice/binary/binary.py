def parse_binary(binary_string):
    if not all(c in "01" for c in binary_string):
        raise ValueError(f"Invalid binary literal: {binary_string}")

    decimal_number = 0
    for digit in binary_string:
        decimal_number = decimal_number * 2 + int(digit)

    return decimal_number