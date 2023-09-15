def largest(min_factor, max_factor):
    """
    Given a range of numbers, find the largest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    palindromes = []
    factors = []
    for i in range(min_factor, max_factor+1):
        for j in range(i, max_factor+1):
            product = i * j
            if str(product) == str(product)[::-1]:
                palindromes.append(product)
                factors.append((i, j))
    
    if palindromes:
        max_palindrome = max(palindromes)
        max_factors = [factor for palindrome, factor in zip(palindromes, factors) if palindrome == max_palindrome]
        return max_palindrome, max_factors
    else:
        return None, []

def smallest(min_factor, max_factor):
    """
    Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    palindromes = []
    factors = []
    for i in range(min_factor, max_factor+1):
        for j in range(i, max_factor+1):
            product = i * j
            if str(product) == str(product)[::-1]:
                palindromes.append(product)
                factors.append((i, j))
    
    if palindromes:
        min_palindrome = min(palindromes)
        min_factors = [factor for palindrome, factor in zip(palindromes, factors) if palindrome == min_palindrome]
        return min_palindrome, min_factors
    else:
        return None, []