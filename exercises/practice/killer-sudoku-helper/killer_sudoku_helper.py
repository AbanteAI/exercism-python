def is_valid_combination(combination, exclude):
    for num in exclude:
        if num in combination:
            return False
    return True

def combinations(target, size, exclude):
    from itertools import combinations as itertools_combinations

    all_combinations = itertools_combinations(range(1, 10), size)
    valid_combinations = []

    for combination in all_combinations:
        if sum(combination) == target and is_valid_combination(combination, exclude):
            valid_combinations.append(sorted(list(combination)))

    return sorted(valid_combinations, key=lambda x: tuple(x))