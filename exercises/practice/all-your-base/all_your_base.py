def rebase(input_base, digits, output_base):
    pass

def from_input_base(digits, input_base):
    number = 0
    for i, digit in enumerate(reversed(digits)):
        number += digit * (input_base ** i)
    return number

def to_output_base(number, output_base):
    digits = []
    while number > 0:
        if number == 0:
            return [0]
        digits.append(number % output_base)
        number //= output_base
    return list(reversed(digits))

def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    number = from_input_base(digits, input_base)
    return to_output_base(number, output_base)