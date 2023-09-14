import itertools
import re

def solve(puzzle):
    words = re.findall(r"[A-Za-z]+", puzzle)
    unique_chars = set("".join(words))
    assert len(unique_chars) <= 10, "Too many letters"
    first_chars = {word[0] for word in words}
    n = len(first_chars)
    sorted_chars = "".join(first_chars) + "".join(unique_chars - first_chars)
    characters = tuple(ord(c) for c in sorted_chars)
    digits = tuple(ord(c) for c in "0123456789")
    zero = digits[0]

    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return dict(zip(sorted_chars, guess))

    return None