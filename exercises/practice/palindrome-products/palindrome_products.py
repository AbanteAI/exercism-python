def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    max_palindrome = 0
    factors = []

    for i in range(max_factor, min_factor - 1, -1):
        for j in range(max_factor, i - 1, -1):
            product = i * j
            if product <= max_palindrome:
                break
            if is_palindrome(product):
                max_palindrome = product
                factors = [i, j]

    return max_palindrome, factors


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    min_palindrome = float('inf')
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if product >= min_palindrome:
                break
            if is_palindrome(product):
                min_palindrome = product
                factors = [i, j]

    return min_palindrome, factors
