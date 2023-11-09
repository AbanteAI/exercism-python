def is_palindrome(number):
    return str(number) == str(number)[::-1]
def largest(min_factor=0, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min_factor must be <= max_factor")

    largest_palindrome = None
    factors = []
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if is_palindrome(product):
                if largest_palindrome is None or product > largest_palindrome:
                    largest_palindrome = product
                    factors = [(i, j)]
                elif product == largest_palindrome:
                    factors.append((i, j))

    return largest_palindrome, factors


def smallest(min_factor=0, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min_factor must be <= max_factor")

    smallest_palindrome = None
    factors = []
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if is_palindrome(product):
                if smallest_palindrome is None or product < smallest_palindrome:
                    smallest_palindrome = product
                    factors = [(i, j)]
                elif product == smallest_palindrome:
                    factors.append((i, j))

    return smallest_palindrome, factors
