def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    
    decimal_value = sum(digit * input_base ** i for i, digit in enumerate(reversed(digits)))
    result = []
    
    while decimal_value > 0:
        decimal_value, remainder = divmod(decimal_value, output_base)
        result.insert(0, remainder)
    
    return result or [0]