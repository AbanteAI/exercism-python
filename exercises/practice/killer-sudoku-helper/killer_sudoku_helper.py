import itertools

def combinations(target, size, exclude):
    digits = [i for i in range(1, 10) if i not in exclude]
    valid_combinations = []

    for combination in itertools.combinations(digits, size):
        if sum(combination) == target:
            valid_combinations.append(sorted(list(combination)))

    return sorted(valid_combinations)
