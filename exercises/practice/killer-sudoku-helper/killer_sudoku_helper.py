from itertools import combinations as it_combinations

    all_combinations = set(it_combinations(range(1, 10), size))
def combinations(target, size, exclude):
    all_combinations = set(combinations(range(1, 10), size))
    valid_combinations = [
        combo for combo in all_combinations
        if sum(combo) == target and not any(num in combo for num in exclude)
    ]
    return sorted(valid_combinations)
