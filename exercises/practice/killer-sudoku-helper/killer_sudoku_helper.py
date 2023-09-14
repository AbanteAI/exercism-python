from itertools import combinations as itertools_combinations


def combinations(target, size, exclude):
    exclude_set = set(exclude)
    all_numbers = set(range(1, 10))
    available_numbers = sorted(list(all_numbers - exclude_set))
    possible_combinations = list(itertools_combinations(available_numbers, size))
    valid_combinations = [list(comb) for comb in possible_combinations if sum(comb) == target]
    return valid_combinations