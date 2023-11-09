from itertools import permutations

def solve(puzzle):
    # Extract words and unique letters from the puzzle
    left, right = puzzle.replace(' ', '').split('==')
    left_words = left.split('+')
    words = left_words + [right]
    unique_letters = set(''.join(words))

    # We can't have more unique letters than digits
    if len(unique_letters) > 10:
        return None

    # Generate all possible permutations of digits
    for perm in permutations('0123456789', len(unique_letters)):
        solution = dict(zip(unique_letters, perm))

        # Check if the solution has any leading zeros
        if any(solution[word[0]] == '0' for word in words):
            continue

        # Replace letters with digits and check if the puzzle is solved
        try:
            left_sum = sum(int("".join(solution[letter] for letter in word)) for word in left_words)
            right_sum = int("".join(solution[letter] for letter in right))
            if left_sum == right_sum:
                return {k: int(v) for k, v in solution.items()}
        except ValueError:
            continue
    return None
