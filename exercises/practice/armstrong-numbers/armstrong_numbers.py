def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    length = len(digits)
    armstrong_sum = sum([d ** length for d in digits])
    return armstrong_sum == number
