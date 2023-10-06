def parse_binary(binary_string):
    decimal = 0
    for i, digit in enumerate(reversed(binary_string)):
        if digit not in '01':
            raise ValueError("Invalid binary literal: " + binary_string)
        decimal += int(digit) * (2 ** i)
    return decimal
