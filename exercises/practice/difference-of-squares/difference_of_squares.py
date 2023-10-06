def square_of_sum(number):
    # Calculate the sum of numbers from 1 to number
    sum_of_numbers = sum(range(1, number + 1))

    # Return the square of the sum
    return sum_of_numbers ** 2


def sum_of_squares(number):
    # Calculate the sum of squares of numbers from 1 to number
    sum_of_squares = sum(i ** 2 for i in range(1, number + 1))

    # Return the sum of squares
    return sum_of_squares


def difference_of_squares(number):
    # Calculate the difference between the square of the sum and the sum of squares
    return square_of_sum(number) - sum_of_squares(number)
