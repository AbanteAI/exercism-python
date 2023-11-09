def parse_binary(binary_string):
    # Check if the binary_string contains only 0's and 1's
    if not all(char in '01' for char in binary_string):
        raise ValueError("Invalid binary literal: " + binary_string)
    # Convert binary string to decimal
    decimal_number = 0
    for digit in binary_string:
        decimal_number = decimal_number * 2 + int(digit)
    return decimal_number
