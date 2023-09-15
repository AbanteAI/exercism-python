def hexa(hex_string):
    decimal = 0
    power = len(hex_string) - 1
    for digit in hex_string:
        if not digit.isnumeric() and not ('a' <= digit <= 'f') and not ('A' <= digit <= 'F'):
            return None
        if digit.isnumeric():
            decimal += int(digit) * (16 ** power)
        else:
            decimal += (ord(digit.lower()) - ord('a') + 10) * (16 ** power)
        power -= 1
    return decimal
    power = len(hex_string) - 1
    for digit in hex_string:
        if not digit.isnumeric() and not ('a' <= digit <= 'f') and not ('A' <= digit <= 'F'):
            return None
        if digit.isnumeric():
            decimal += int(digit) * (16 ** power)
        else:
            decimal += (ord(digit.lower()) - ord('a') + 10) * (16 ** power)
        power -= 1
    return decimal
