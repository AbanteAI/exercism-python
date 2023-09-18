def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min_factor must be <= max_factor.")
    palindromes = {}
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if is_palindrome(product):
                if product in palindromes:
                    palindromes[product].append((i, j))
                else:
                    palindromes[product] = [(i, j)]

    if not palindromes:
        raise ValueError("No palindrome products in the given range.")
    largest_palindrome = max(palindromes.keys())
    return largest_palindrome, palindromes[largest_palindrome]
    pass
def is_palindrome(number):
    return str(number) == str(number)[::-1]


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    if min_factor > max_factor:
        raise ValueError("min_factor must be <= max_factor.")
    """

    palindromes = {}
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if is_palindrome(product):
                if product in palindromes:
                    palindromes[product].append((i, j))
                else:
                    palindromes[product] = [(i, j)]

    if not palindromes:
        raise ValueError("No palindrome products in the given range.")
    smallest_palindrome = min(palindromes.keys())
    return smallest_palindrome, palindromes[smallest_palindrome]
