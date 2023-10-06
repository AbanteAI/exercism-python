from itertools import permutations
    words = puzzle.split()
    unique_chars = set("".join(words))
    if len(unique_chars) > 10:
        return {}
    
    chars = "".join(unique_chars)
    for perm in permutations(range(10), len(unique_chars)):
        mapping = dict(zip(chars, perm))
        if all(mapping[word[0]] != 0 for word in words):
            left = int("".join(str(mapping[char]) for char in words[-1]))
            right = sum(int("".join(str(mapping[char]) for char in word)) for word in words[:-1])
            if left == right:
                return mapping
    return {}
