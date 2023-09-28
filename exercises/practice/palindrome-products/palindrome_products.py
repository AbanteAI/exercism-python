def is_palindrome(number):
    return str(number) == str(number)[::-1]
def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    
    for product in range(max_factor * max_factor, min_factor * min_factor - 1, -1):
        if is_palindrome(product):
            factors = [(i, product // i) for i in range(min_factor, max_factor + 1) if product % i == 0 and min_factor <= product // i <= max_factor]
            if factors:
                return product, factors
    return None, []


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    
    for product in range(min_factor * min_factor, (max_factor * max_factor) + 1):
        if is_palindrome(product):
            factors = [(i, product // i) for i in range(min_factor, max_factor + 1) if product % i == 0 and min_factor <= product // i <= max_factor]
            if factors:
                return product, factors
    return None, []
