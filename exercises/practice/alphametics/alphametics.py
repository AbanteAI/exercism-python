def solve(puzzle):
    import itertools
    import re

    # Function to replace letters with digits in the puzzle
    def substitute(expression, solution):
        return expression.translate(str.maketrans(solution))

    # Extract all words from the puzzle
    words = re.findall("[A-Z]+", puzzle)

    # Extract unique letters to be used as keys for permutations
    unique_letters = set(''.join(words))

    # Leading letters cannot be zero, so we store them to enforce this rule
    leading_letters = {word[0] for word in words}

    # Generate all possible digit assignments to letters
    for digits in itertools.permutations('0123456789', len(unique_letters)):
        solution = dict(zip(unique_letters, map(int, digits)))  # Map letters to integers

        # Skip if any leading letter is assigned a '0'
        if any(solution[letter] == 0 for letter in leading_letters):
            continue

        # Substitute letters in the puzzle with digits from the current solution
        substituted_expression = substitute(puzzle, {k: str(v) for k, v in solution.items()})

        # Split the expression into left and right sides of the equation
        left, right = substituted_expression.split('=')
        try:
            # Evaluate both sides to check if the solution is correct
            if eval(left) == eval(right):
                return {k: v for k, v in solution.items()}  # Return the solution with integer values
        except ZeroDivisionError:
            continue
        except ZeroDivisionError:
            continue

    # If no solution is found, return None
    return None