def trinary(string):
    # Validate the input string
    if not all(char in '012' for char in string):
        return 0

    # Calculate the decimal equivalent
    decimal_value = 0
    for index, digit in enumerate(reversed(string)):
        decimal_value += int(digit) * (3 ** index)

    return decimal_value
