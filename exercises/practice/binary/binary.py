def parse_binary(binary_string):
    decimal = 0
    power = len(binary_string) - 1
    for digit in binary_string:
        if digit == '1':
            decimal += 2 ** power
        elif digit != '0':
            raise ValueError("Invalid binary string")
        power -= 1
    return decimal
