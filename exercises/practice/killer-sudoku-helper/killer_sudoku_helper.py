from itertools import combinations

def combinations(target, size, exclude):
    """
    Generate all valid combinations of digits for a Killer Sudoku cage.

    :param target: The target sum of the digits in the cage.
    :param size: The number of digits in the cage.
    :param exclude: A list of digits to exclude from the combinations.
    :return: A list of valid combinations, each combination is a tuple of digits.
    """
    all_digits = set(range(1, 10)) - set(exclude)
    all_combinations = list(combinations(all_digits, size))
    valid_combinations = [combo for combo in all_combinations if sum(combo) == target and len(set(combo)) == size]
    return sorted(valid_combinations)