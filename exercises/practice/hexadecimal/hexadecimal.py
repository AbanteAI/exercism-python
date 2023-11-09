def hexa(hex_string):
    hex_digits = '0123456789abcdef'
    decimal_value = 0

    try:
        for char in hex_string.lower():
            decimal_value = decimal_value * 16 + hex_digits.index(char)
    except ValueError:
        raise ValueError("Invalid hexadecimal string")

    return decimal_value