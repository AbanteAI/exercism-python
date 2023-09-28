import itertools
import re

def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_chars = set(''.join(words))
    assert len(unique_chars) <= 10, 'Too many letters'
    first_chars = {word[0] for word in words}
    sorted_chars = ''.join(first_chars) + ''.join(unique_chars - first_chars)
    characters = tuple(ord(c) for c in sorted_chars)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]

    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:len(first_chars)]:
            trans = dict(zip(characters, guess))
            if sum(sum(trans[ord(c)] for c in word) for word in words[:-1]) == sum(trans[ord(c)] for c in words[-1]):
                return {chr(k): v - ord('0') for k, v in trans.items()}
    return None