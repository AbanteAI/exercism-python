def hexa(hex_string):
    if not all(c in '0123456789abcdefABCDEF' for c in hex_string):
        raise ValueError("Invalid hexadecimal string")

    decimal_value = 0
    for digit in hex_string:
        decimal_value = decimal_value * 16 + int(digit, 16)
    return decimal_value