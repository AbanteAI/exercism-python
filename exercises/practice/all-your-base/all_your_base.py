def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError("input base must be >= 2")

    if any(digit < 0 or digit >= input_base for digit in digits):
        raise ValueError("Invalid digits for input base")

    decimal_value = sum(digit * input_base ** (len(digits) - i - 1) for i, digit in enumerate(digits))
    if decimal_value == 0:
        return [0]

    result = []
    while decimal_value > 0:
        result.append(decimal_value % output_base)
        decimal_value //= output_base

    return result[::-1]
