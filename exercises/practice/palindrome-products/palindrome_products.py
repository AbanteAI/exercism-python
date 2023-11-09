def is_palindrome(number):
    return str(number) == str(number)[::-1]

def largest(min_factor=0, max_factor=None):
    if max_factor is None or min_factor > max_factor:
        raise ValueError("min_factor must be <= max_factor")
    largest_palindrome = 0
    factors = []
    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):
            product = i * j
            if is_palindrome(product):
                if product > largest_palindrome:
                    largest_palindrome = product
                    factors = [(i, j)]
                elif product == largest_palindrome:
                    factors.append((i, j))
                break  # Break out of the loop early for optimization
    factors.sort()
    return largest_palindrome, factors


def smallest(min_factor=0, max_factor=None):
    if max_factor is None or min_factor > max_factor:
        raise ValueError("min_factor must be <= max_factor")
    smallest_palindrome = max_factor**2 + 1
    factors = []
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if is_palindrome(product) and product < smallest_palindrome:
                smallest_palindrome = product
                factors = [(i, j)]
                break  # Break out of the loop early for optimization
            elif product == smallest_palindrome:
                factors.append((i, j))
    if smallest_palindrome == max_factor**2 + 1:
        return None, []
    factors.sort()
    return smallest_palindrome, factors
