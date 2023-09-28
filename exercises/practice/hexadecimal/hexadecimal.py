def hexa(hex_string):
    decimal = 0
    hex_digits = "0123456789abcdef"
    for digit in hex_string.lower():
        if digit not in hex_digits:
            return 0
        decimal = decimal * 16 + hex_digits.index(digit)
    return decimal
