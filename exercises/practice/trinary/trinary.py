def trinary(string):
    try:
        # Validate the trinary string
        if not all(char in '012' for char in string):
            return 0

        # Convert trinary to decimal
        decimal = 0
        for index, digit in enumerate(reversed(string)):
            decimal += int(digit) * (3 ** index)
        return decimal
    except (TypeError, ValueError):
        # In case of an exception, consider it an invalid trinary string
        return 0