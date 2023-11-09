def trinary(string):
    # Check if the string is a valid trinary
    if not all(char in '012' for char in string):
        return 0

    # Convert trinary to decimal
    decimal = 0
    for index, digit in enumerate(reversed(string)):
        decimal += int(digit) * (3 ** index)

    return decimal
