def parse_binary(binary_string):
    decimal = 0
    power = len(binary_string) - 1
    for digit in binary_string:
        if digit not in ['0', '1']:
            raise ValueError("Invalid binary literal: " + binary_string)
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal
