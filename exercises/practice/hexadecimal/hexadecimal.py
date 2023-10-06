def hexa(hex_string):
    hex_chars = '0123456789abcdef'
    hex_string = hex_string.lower()

    for char in hex_string:
        if char not in hex_chars:
            raise ValueError("Invalid hexadecimal string")

    decimal = 0
    power = len(hex_string) - 1

    for char in hex_string:
        decimal += hex_chars.index(char) * (16 ** power)
        power -= 1

    return decimal