def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError("input base must be >= 2")
    
    decimal_value = 0
    for i, digit in enumerate(reversed(digits)):
            raise ValueError("Invalid digit")
            raise ValueError("Invalid digit")
        decimal_value += digit * (input_base ** i)
    
        return [0]
        return [0]
    
    converted_digits = []
    while decimal_value > 0:
        converted_digits.insert(0, decimal_value % output_base)
        decimal_value //= output_base
    
    return converted_digits
