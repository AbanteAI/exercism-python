def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    base_10 = sum(d * input_base ** i for i, d in enumerate(reversed(digits)))
    converted_digits = []
    while base_10 > 0:
        base_10, remainder = divmod(base_10, output_base)
        converted_digits.append(remainder)
    return list(reversed(converted_digits))

