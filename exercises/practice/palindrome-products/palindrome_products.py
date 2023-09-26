def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Invalid input: min_factor is greater than max_factor")

    max_palindrome = None
    factors = []

    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):
            product = i * j
            if is_palindrome(product):
                if max_palindrome is None or product > max_palindrome:
                    max_palindrome = product
                    factors = [(j, i)]
                elif product == max_palindrome:
                    factors.append((j, i))

    return max_palindrome, factors


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Invalid input: min_factor is greater than max_factor")

    min_palindrome = None
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if is_palindrome(product):
                if min_palindrome is None or product < min_palindrome:
                    min_palindrome = product
                    factors = [(i, j)]
                elif product == min_palindrome:
                    factors.append((i, j))

    return min_palindrome, factors


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Invalid input: min_factor is greater than max_factor")

    min_palindrome = None
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if is_palindrome(product):
                if min_palindrome is None or product < min_palindrome:
                    min_palindrome = product
                    factors = [(i, j)]
                elif product == min_palindrome:
                    factors.append((i, j))

    return min_palindrome, factors