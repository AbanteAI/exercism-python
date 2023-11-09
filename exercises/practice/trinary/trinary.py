def trinary(string):
    # Validate the trinary string
    if not all(char in '012' for char in string):
        return 0

    # Convert trinary to decimal
    decimal_value = 0
    for index, digit in enumerate(reversed(string)):
        decimal_value += int(digit) * (3 ** index)

    return decimal_value
