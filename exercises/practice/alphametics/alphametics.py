from itertools import permutations

def solve(puzzle):
    # Extract unique letters from puzzle
    letters = ''.join(set(filter(str.isalpha, puzzle)))
    
    # Extract words from the puzzle
    words = puzzle.replace(' ', '').replace('+', ' ').replace('==', ' ').split()
    first_letters = {word[0] for word in words if word[0].isalpha()}
    
    # Generate all possible assignments of digits to letters
    for perm in permutations('0123456789', len(letters)):
        solution = dict(zip(letters, perm))
        
        # Skip solutions that assign 0 to any first letter of a word
        if any(solution[letter] == '0' for letter in first_letters):
            continue
        
        # Convert words to numbers using the current permutation
        try:
            numbers = [int("".join(solution[c] for c in word)) for word in words]
            if sum(numbers[:-1]) == numbers[-1]:
                return {k: int(v) for k, v in solution.items()}
        except ValueError:
            continue
    
    # If no solution is found
    return None
