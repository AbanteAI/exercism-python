def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    pass


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    pass
def is_palindrome(number):
    return str(number) == str(number)[::-1]

def find_palindromes(min_factor, max_factor):
    palindromes = set()

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if is_palindrome(product):
                palindromes.add((product, (i, j)))

    largest_palindrome = max(palindromes, key=lambda x: x[0])
    smallest_palindrome = min(palindromes, key=lambda x: x[0])

    return largest_palindrome, smallest_palindrome

def largest(min_factor, max_factor):
    return find_palindromes(min_factor, max_factor)[0]

def smallest(min_factor, max_factor):
    return find_palindromes(min_factor, max_factor)[1]
