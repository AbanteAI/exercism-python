def trinary(string):
    if not all(c in "012" for c in string):
        return 0

    decimal_value = 0
    for i, c in enumerate(reversed(string)):
        decimal_value += int(c) * (3 ** i)

    return decimal_value