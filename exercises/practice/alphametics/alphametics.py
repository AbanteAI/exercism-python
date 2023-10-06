def permutations(digits, length):
    if length == 0:
        yield []
    else:
        for i, digit in enumerate(digits):
            for perm in permutations(digits[:i] + digits[i + 1:], length - 1):
                yield [digit] + perm

def solve(puzzle):
    words = puzzle.replace(' + ', ' ').replace(' = ', ' ').split()
    unique_chars = set(''.join(words))
    leading_chars = set(word[0] for word in words)
    chars = ''.join(unique_chars)
    digits = ''.join(str(d) for d in range(10))
    for perm in permutations(digits, len(unique_chars)):
        if '0' in perm and any(char in perm for char in leading_chars):
            continue
        table = str.maketrans(chars, ''.join(perm))
        equation = puzzle.translate(table)
        if eval(equation):
            return {char: int(perm[i]) for i, char in enumerate(chars)}
    return {}