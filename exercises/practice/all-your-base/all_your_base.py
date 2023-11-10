def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # Convert input digits to base 10
    number_in_base_10 = 0
    for index, digit in enumerate(reversed(digits)):
        number_in_base_10 += digit * (input_base ** index)

    # Handle the special case where the number is 0
    if number_in_base_10 == 0:
        return [0]

    # Convert base 10 number to the output base
    output_digits = []
    while number_in_base_10 > 0:
        number_in_base_10, remainder = divmod(number_in_base_10, output_base)
        output_digits.append(remainder)

    return list(reversed(output_digits))