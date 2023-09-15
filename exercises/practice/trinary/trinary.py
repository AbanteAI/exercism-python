def trinary(string):
    if any(char not in "012" for char in string):
        return 0

    decimal = 0
    for i, digit in enumerate(reversed(string)):
        decimal += int(digit) * (3 ** i)

    return decimal