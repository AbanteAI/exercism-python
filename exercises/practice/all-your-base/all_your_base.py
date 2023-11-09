def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # Convert input digits to decimal
    decimal_number = 0
    for i, digit in enumerate(reversed(digits)):
        decimal_number += digit * (input_base ** i)

    # Convert decimal to output base
    if decimal_number == 0:
        return [0]

    output_digits = []
    while decimal_number > 0:
        output_digits.append(decimal_number % output_base)
        decimal_number //= output_base

    return list(reversed(output_digits))
