def hexa(hex_string):
    if not all(c in "0123456789abcdefABCDEF" for c in hex_string):
        raise ValueError("Invalid hexadecimal string")

    decimal_value = 0
    for i, c in enumerate(reversed(hex_string)):
        decimal_value += int(c, 16) * (16 ** i)

    return decimal_value
