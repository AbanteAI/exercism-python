def hexa(hex_string):
    hex_digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                  'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                  'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    decimal_value = 0

    for digit in hex_string:
        if digit not in hex_digits:
            raise ValueError("Invalid hexadecimal digit")
        decimal_value = decimal_value * 16 + hex_digits[digit]

    return decimal_value