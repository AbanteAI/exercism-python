def hexa(hex_string):
    hex_values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                  'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

    if any(c.lower() not in hex_values for c in hex_string):
        raise ValueError("Invalid hexadecimal string")

    decimal_value = 0
    for c in hex_string:
        decimal_value = decimal_value * 16 + hex_values[c.lower()]

    return decimal_value