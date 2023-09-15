def rebase(input_base, digits, output_base):
    # Convert input_base to decimal
    decimal = 0
    power = len(digits) - 1
    for digit in digits:
        decimal += digit * (input_base ** power)
        power -= 1
    
    # Convert decimal to output_base
    result = []
    while decimal > 0:
        remainder = decimal % output_base
        result.insert(0, remainder)
        decimal = decimal // output_base
    
    return result