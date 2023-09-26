def hexa(hex_string):
    hex_digits = "0123456789abcdef"
    decimal = 0
    power = len(hex_string) - 1

    for digit in hex_string:
        if digit.lower() not in hex_digits:
    if not hex_string:
        raise ValueError("Invalid hexadecimal string")
    if not all(digit.lower() in hex_digits for digit in hex_string):
        raise ValueError("Invalid hexadecimal string")
    if not all(digit.lower() in hex_digits for digit in hex_string):
        raise ValueError("Invalid hexadecimal string")
    if not all(digit.lower() in hex_digits for digit in hex_string):
        raise ValueError("Invalid hexadecimal string")
    if not all(digit.lower() in hex_digits for digit in hex_string):
        raise ValueError("Invalid hexadecimal string")
    return decimal
