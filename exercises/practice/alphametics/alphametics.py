def solve(puzzle):
from itertools import permutations
    words, result = puzzle.upper().replace(" ", "").split("==")
    unique_letters = set(puzzle.replace(" ", ""))
    leading_letters = set(word[0] for word in words) | set(result[0])
    letters = ''.join(unique_letters)
    digits = range(10)
    for perm in permutations(digits, len(unique_letters)):
        if 0 in perm:
            continue
        digit_map = dict(zip(unique_letters, perm))
        if any(digit_map[w[0]] == 0 for w in leading_letters):
            continue
        if sum(digit_map[w] for w in words) == sum(digit_map[w] for w in result):
            return digit_map
    return {}