def parse_binary(binary_string):
    if not all(char in '01' for char in binary_string):
        raise ValueError(f"Invalid binary literal: {binary_string}")

    decimal_number = int(binary_string, 2)
    return decimal_number