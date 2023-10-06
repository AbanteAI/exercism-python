def trinary(string):
    decimal = 0
    for i, digit in enumerate(reversed(string)):
        if digit not in {'0', '1', '2'}:
            return 0
        decimal += int(digit) * (3 ** i)
    return decimal

