def is_armstrong_number(number):
    num_digits = len(str(number))
    armstrong_sum = sum(int(digit) ** num_digits for digit in str(number))
    return armstrong_sum == number