def rebase(input_base, digits, output_base):
    pass
def to_base_10(input_base, digits):
    number = 0
    for i, digit in enumerate(reversed(digits)):
        number += digit * (input_base ** i)
    return number

def from_base_10(output_base, number):
    if number == 0:
        return [0]
    digits = []
    while number > 0:
        number, remainder = divmod(number, output_base)
        digits.append(remainder)
    return digits[::-1]

def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if len(digits) == 0:
        return []

    number_base_10 = to_base_10(input_base, digits)
    return from_base_10(output_base, number_base_10)
