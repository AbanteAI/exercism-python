from itertools import permutations

def solve(puzzle):
    # Helper function to convert a word to a number according to the current assignment
    def word_to_number(word, letter_to_digit):
        return int(''.join(str(letter_to_digit[letter]) for letter in word))

    # Parse the puzzle into operands and result
    operands, result = puzzle.replace(' == ', '==').split('==')
    operands = operands.split(' + ')

    # Extract unique letters from the puzzle
    unique_letters = set(''.join(operands) + result)

    # Check if the puzzle is solvable (more letters than digits)
    if len(unique_letters) > 10:
        return None

    # Generate all possible assignments of digits to letters
    for perm in permutations('0123456789', len(unique_letters)):
        letter_to_digit = dict(zip(unique_letters, perm))

        # Skip if any operand or the result has a leading zero
        if any(letter_to_digit[word[0]] == '0' for word in operands + [result]):
            continue

        # Convert operands and result to numbers based on the current assignment
        converted_operands = [word_to_number(word, letter_to_digit) for word in operands]
        converted_result = word_to_number(result, letter_to_digit)

        # Check if the current assignment solves the puzzle
        if sum(converted_operands) == converted_result:
            # Return the correct assignment
            return {letter: int(digit) for letter, digit in letter_to_digit.items()}

    # If no solution is found
    return None
