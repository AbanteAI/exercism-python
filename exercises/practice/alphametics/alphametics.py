import re
from itertools import permutations
def solve(puzzle):
    words = [word.strip() for word in re.split('[+=]', puzzle) if word.strip()]
    unique_chars = set("".join(words))
    assert len(unique_chars) <= 10, "Too many unique characters"

    for perm in permutations("0123456789", len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        if all(mapping[word[0]] != "0" for word in words):
            translated_words = [int("".join([mapping[char] for char in word])) for word in words]
            if sum(translated_words[:-1]) == translated_words[-1]:
                return mapping

    return None