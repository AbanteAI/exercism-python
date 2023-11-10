def largest(min_factor=0, max_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor must be <= max_factor")
    max_palindrome = 0
    factors = []
    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):
            product = i * j
            if str(product) == str(product)[::-1]:
                if product > max_palindrome:
                    max_palindrome = product
                    factors = [(i, j)]
                elif product == max_palindrome:
                    factors.append((i, j))
    return max_palindrome, sorted(factors)


def smallest(min_factor=0, max_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor must be <= max_factor")
    min_palindrome = None
    factors = []
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if str(product) == str(product)[::-1]:
                if min_palindrome is None or product < min_palindrome:
                    min_palindrome = product
                    factors = [(i, j)]
                elif product == min_palindrome:
                    factors.append((i, j))
    return min_palindrome, sorted(factors)
