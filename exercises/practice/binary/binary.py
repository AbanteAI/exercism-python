def parse_binary(binary_string):
    # Check if the binary_string is a valid binary number
    if not all(char in '01' for char in binary_string):
        raise ValueError("Invalid binary literal: " + binary_string)

    # Convert binary to decimal
    decimal = 0
    for index, digit in enumerate(reversed(binary_string)):
        decimal += int(digit) * (2 ** index)
    return decimal