def largest(min_factor=0, max_factor=None):
    if max_factor is None or min_factor > max_factor:
        raise ValueError("min must be <= max")
    largest_palindrome = None
    factors = set()
    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):
            product = i * j
            if str(product) == str(product)[::-1]:
                if largest_palindrome is None or product > largest_palindrome:
                    largest_palindrome = product
                    factors = {(i, j)}
                elif product == largest_palindrome:
                    factors.add((i, j))
    if largest_palindrome is None:
        return None, []
    return largest_palindrome, sorted(factors)


def smallest(min_factor=0, max_factor=None):
    if max_factor is None or min_factor > max_factor:
        raise ValueError("min must be <= max")
    smallest_palindrome = None
    factors = set()
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if str(product) == str(product)[::-1]:
                if smallest_palindrome is None or product < smallest_palindrome:
                    smallest_palindrome = product
                    factors = {(i, j)}
                elif product == smallest_palindrome:
                    factors.add((i, j))
    if smallest_palindrome is None:
        return None, []
    return smallest_palindrome, sorted(factors)
