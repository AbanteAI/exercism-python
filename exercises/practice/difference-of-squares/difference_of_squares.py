def square_of_sum(number):
    # Calculate the sum of the first N natural numbers
    sum_of_numbers = sum(range(1, number + 1))
    # Calculate the square of the sum
    square_of_sum = sum_of_numbers ** 2
    return square_of_sum


def sum_of_squares(number):
    # Calculate the sum of the squares of the first N natural numbers
    sum_of_squares = sum([x ** 2 for x in range(1, number + 1)])
    return sum_of_squares


def difference_of_squares(number):
    # Calculate the difference between the square of the sum and the sum of the squares
    difference = square_of_sum(number) - sum_of_squares(number)
    return difference