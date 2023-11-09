from itertools import combinations as itertools_combinations

def combinations(target, size, exclude):
    """
    Generate all valid combinations of digits for a given cage in a Killer Sudoku puzzle.

    :param target: The target sum of the digits in the cage.
    :param size: The number of cells in the cage.
    :param exclude: A list of digits that are already used in the row/column/box.
    :return: A sorted list of lists, each representing a valid combination of digits.
    """
    valid_digits = [digit for digit in range(1, 10) if digit not in exclude]
    all_combinations = list(itertools_combinations(valid_digits, size))
    valid_combinations = [list(combo) for combo in all_combinations if sum(combo) == target and len(set(combo)) == size]
    return sorted(valid_combinations)
