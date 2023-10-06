def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    palindromes = []
    for i in range(max_factor, min_factor - 1, -1):
        if i * i < palindromes[-1][0] if palindromes else float('inf'):
            break
        for j in range(i, min_factor - 1, -1):
            product = i * j
            if product < palindromes[-1][0] if palindromes else float('inf'):
                break
            if str(product) == str(product)[::-1]:
                palindromes.append((product, {i, j}))

    if not palindromes:
        raise ValueError("No palindrome product found")

    max_palindrome = max(palindromes, key=lambda x: x[0])
    return max_palindrome


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    palindromes = []
    for i in range(min_factor, max_factor + 1):
        if i * i > palindromes[-1][0] if palindromes else float('-inf'):
            break
        for j in range(i, max_factor + 1):
            product = i * j
            if product > palindromes[-1][0] if palindromes else float('-inf'):
                break
            if str(product) == str(product)[::-1]:
                palindromes.append((product, {i, j}))

    if not palindromes:
        raise ValueError("No palindrome product found")

    min_palindrome = min(palindromes, key=lambda x: x[0])
    return min_palindrome


