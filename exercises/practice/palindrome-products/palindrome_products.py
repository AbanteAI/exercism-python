def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
def largest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("min must be <= max")

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
        raise ValueError("No palindromes found")

    largest = max(palindromes.keys())
    return largest, palindromes[largest]
def is_palindrome(number):
    return str(number) == str(number)[::-1]


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

def smallest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("min must be <= max")

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
        raise ValueError("No palindromes found")

    smallest = min(palindromes.keys())
    return smallest, palindromes[smallest]
