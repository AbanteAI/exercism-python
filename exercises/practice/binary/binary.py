def parse_binary(binary_string):
    if not all(char in '01' for char in binary_string):
        raise ValueError("Invalid binary literal: " + binary_string)
    
    decimal_value = 0
    for index, digit in enumerate(reversed(binary_string)):
        decimal_value += int(digit) * (2 ** index)
    
    return decimal_value
