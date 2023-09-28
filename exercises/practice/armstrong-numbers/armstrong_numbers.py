def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    num_digits = len(digits)
    sum_of_digits = sum([digit ** num_digits for digit in digits])
    return sum_of_digits == number
