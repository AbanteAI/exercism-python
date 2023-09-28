def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    number_in_base_10 = 0
    for i, digit in enumerate(reversed(digits)):
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        number_in_base_10 += digit * (input_base ** i)

    if number_in_base_10 == 0:
        return [0]

    result = []
    while number_in_base_10 > 0:
        number_in_base_10, remainder = divmod(number_in_base_10, output_base)
        result.append(remainder)

    return result[::-1]