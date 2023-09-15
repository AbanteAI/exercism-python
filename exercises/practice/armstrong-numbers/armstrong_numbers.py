def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    power = len(digits)
    digit_sum = sum([digit ** power for digit in digits])
    return digit_sum == number
