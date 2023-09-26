from itertools import permutations
def solve(puzzle):
    words = puzzle.split()
    unique_letters = set(''.join(words))
    leading_letters = set(word[0] for word in words)
    if len(unique_letters) > 10 or len(leading_letters) > 10:
        return {}
    letters = ''.join(unique_letters)
        for permutation in permutations('0123456789', len(letters)):
        mapping = str.maketrans(letters, ''.join(permutation))
        if '0' not in permutation[:len(leading_letters)]:
            equation = puzzle.translate(mapping)
            if eval(equation):
                return {letter: int(permutation[i]) for i, letter in enumerate(letters)}
    return {}