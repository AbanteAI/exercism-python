from itertools import permutations

def solve(puzzle):
    # Extract unique letters from puzzle
    letters = ''.join(set(filter(str.isalpha, puzzle)))
    digits = '0123456789'
    len_letters = len(letters)

    # Extract words from the puzzle
    words = puzzle.replace(' ', '').replace('+', ' ').replace('==', ' ').split()

    # Function to check if the solution is valid
    def is_valid(mapping):
        if any(mapping[word[0]] == '0' for word in words if len(word) > 1):  # Leading zero check
            return False
        try:
            # Replace letters with digits and check if the sum is correct
            equation = puzzle.translate(str.maketrans(mapping))
            left, right = equation.split('==')
            return sum(int(part) for part in left.split('+')) == int(right)
        except ValueError:
            return False

    # Try all permutations of digits for the letters
    for perm in permutations(digits, len_letters):
        mapping = dict(zip(letters, perm))
        if is_valid(mapping):
            return {letter: int(digit) for letter, digit in mapping.items()}
    return None
