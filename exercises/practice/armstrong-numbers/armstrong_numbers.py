def is_armstrong_number(number):
    # Convert the number to a string to easily iterate over its digits
    digits = str(number)
    num_digits = len(digits)
    # Calculate the sum of the digits each raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    # Check if the calculated sum is equal to the original number
    return armstrong_sum == number
