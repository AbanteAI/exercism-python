def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Invalid range")

    palindromes = []
    factors = []

    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):
            product = i * j
            if str(product) == str(product)[::-1]:
                if not palindromes:
                    palindromes.append(product)
                    factors.append((i, j))
                elif product > palindromes[0]:
                    palindromes = [product]
                    factors = [(i, j)]
                elif product == palindromes[0]:
                    factors.append((i, j))

    return palindromes[0], factors

def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Invalid range")

    palindromes = []
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if str(product) == str(product)[::-1]:
                if not palindromes:
                    palindromes.append(product)
                    factors.append((i, j))
                elif product < palindromes[0]:
                    palindromes = [product]
                    factors = [(i, j)]
                elif product == palindromes[0]:
                    factors.append((i, j))

    return palindromes[0], factors

def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Invalid range")

    palindromes = []
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if str(product) == str(product)[::-1]:
                if not palindromes:
                    palindromes.append(product)
                    factors.append((i, j))
                elif product < palindromes[0]:
                    palindromes = [product]
                    factors = [(i, j)]
                elif product == palindromes[0]:
                    factors.append((i, j))

    return palindromes[0], factors