def parse_binary(binary_string):
    if not all(char in '01' for char in binary_string):
        raise ValueError("Invalid binary literal: " + binary_string)
    
    decimal_value = 0
    for char in binary_string:
        decimal_value = decimal_value * 2 + int(char)
    return decimal_value
