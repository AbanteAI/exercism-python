def hexa(hex_string):
    hex_digits = '0123456789abcdef'
    decimal_value = 0

    try:
        for char in hex_string:
            decimal_value = decimal_value * 16 + hex_digits.index(char.lower())
    except ValueError:
        raise ValueError(f"Invalid hexadecimal string: {hex_string}")

    return decimal_value
