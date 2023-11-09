def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # Convert input digits to base 10
    number_in_base_10 = 0
    for digit in digits:
        number_in_base_10 = number_in_base_10 * input_base + digit

    # Special case for number 0
    if number_in_base_10 == 0:
        return [0]

    # Convert base 10 number to output base
    output_digits = []
    while number_in_base_10 > 0:
        output_digits.insert(0, number_in_base_10 % output_base)
        number_in_base_10 //= output_base

    return output_digits
