from itertools import permutations

def solve(puzzle):
from itertools import permutations

def solve(puzzle):
    words = puzzle.replace(" ", "").split("+")
    result = words.pop(-1)
    words = words[:-1] + [result.split("=")[0], result.split("=")[1]]
    unique_letters = sorted(list(set("".join(words))))
    
    if len(unique_letters) > 10:
        return None

    for perm in permutations("0123456789", len(unique_letters)):
        if "0" not in (perm[unique_letters.index(words[0][0])], perm[unique_letters.index(words[1][0])], perm[unique_letters.index(result[0])]):
            trans = str.maketrans("".join(unique_letters), "".join(perm))
            num_words = [int(w.translate(trans)) for w in words]
            if sum(num_words[:-1]) == num_words[-1]:
                return {unique_letters[i]: int(perm[i]) for i in range(len(unique_letters))}

    return None
