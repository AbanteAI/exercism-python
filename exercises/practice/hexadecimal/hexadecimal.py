def hexa(hex_string):
    hex_digits = '0123456789abcdef'
    try:
        decimal_value = 0
        for char in hex_string:
            decimal_value = decimal_value * 16 + hex_digits.index(char.lower())
        return decimal_value
    except ValueError:
        raise ValueError("Invalid hexadecimal string")