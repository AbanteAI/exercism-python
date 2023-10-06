def hexa(hex_string):
def hexa(hex_string):
    if not all(c in "0123456789abcdefABCDEF" for c in hex_string):
        raise ValueError("Invalid hexadecimal string")

    decimal_value = 0
    power = len(hex_string) - 1

    for char in hex_string:
        if char.isdigit():
            value = int(char)
        else:
            value = 10 + ord(char.lower()) - ord('a')
        decimal_value += value * (16 ** power)
        power -= 1

    return decimal_value
