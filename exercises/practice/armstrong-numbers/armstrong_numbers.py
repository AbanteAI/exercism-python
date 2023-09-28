def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    num_digits = len(digits)
    armstrong_sum = sum(digit ** num_digits for digit in digits)
    return number == armstrong_sum