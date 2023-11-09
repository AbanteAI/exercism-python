def hexa(hex_string):
    hex_digits = '0123456789abcdef'
    decimal_value = 0

    try:
        hex_string = hex_string.lower()
        for index, char in enumerate(reversed(hex_string)):
            decimal_value += hex_digits.index(char) * (16 ** index)
    except ValueError:
        raise ValueError(f"Invalid hexadecimal string: {hex_string}")

    return decimal_value
