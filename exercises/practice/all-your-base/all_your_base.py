def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    decimal = sum(d * input_base**i for i, d in enumerate(digits[::-1]))
    
    result = []
    while decimal > 0:
        result.append(decimal % output_base)
        decimal //= output_base
    
    return result[::-1] if result else [0]
