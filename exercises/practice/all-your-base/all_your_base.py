def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError("input base and output base must be >= 2")
    
    decimal_number = 0
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        decimal_number = decimal_number * input_base + digit

    if decimal_number == 0:
        return [0]

    result = []
    while decimal_number > 0:
        decimal_number, remainder = divmod(decimal_number, output_base)
        result.append(remainder)

    return result[::-1]