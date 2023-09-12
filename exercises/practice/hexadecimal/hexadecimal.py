def hexa(hex_string):
    hex_digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                  'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    hex_string = hex_string.lower()
    decimal_value = 0

    for char in hex_string:
        if char not in hex_digits:
            raise ValueError("Invalid hexadecimal string")

        decimal_value = decimal_value * 16 + hex_digits[char]

    return decimal_value