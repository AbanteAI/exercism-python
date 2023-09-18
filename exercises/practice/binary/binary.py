def parse_binary(binary_string):
    if any(c not in ('0', '1') for c in binary_string):
        raise ValueError(f"Invalid binary literal: {binary_string}")
    
    decimal = 0
    for i, digit in enumerate(reversed(binary_string)):
        decimal += int(digit) * (2 ** i)
    
    return decimal
