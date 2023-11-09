def is_palindrome(number):
    return str(number) == str(number)[::-1]

def find_palindromes(min_factor, max_factor):
def find_palindromes(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor must be <= max_factor")
    palindromes = {}
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if is_palindrome(product):
                if product not in palindromes:
                    palindromes[product] = []
                palindromes[product].append((i, j))
    return palindromes
def largest(*, min_factor, max_factor):
    palindromes = find_palindromes(min_factor, max_factor)
    largest_palindrome = max(palindromes.keys(), default=None)
    factors = palindromes.get(largest_palindrome, [])
    return largest_palindrome, factors


def smallest(*, min_factor, max_factor):
    palindromes = find_palindromes(min_factor, max_factor)
    smallest_palindrome = min(palindromes.keys(), default=None)
    factors = palindromes.get(smallest_palindrome, [])
    return smallest_palindrome, factors
