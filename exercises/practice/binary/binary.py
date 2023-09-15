def parse_binary(binary_string):
    if not all(char in ('0', '1') for char in binary_string):
        raise ValueError(f"Invalid binary literal: {binary_string}")

    decimal_value = 0
    for i, char in enumerate(reversed(binary_string)):
        decimal_value += int(char) * (2 ** i)

    return decimal_value
