import itertools
import ast
import re
def solve(puzzle):
    pass
def extract_unique_letters(puzzle):
    return sorted(set(re.sub(r"[^A-Z]", "", puzzle)))


def evaluate_expression(expression):
    tokens = re.split(r"([+\-*/])", expression)
    result = int(tokens[0])

    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = int(tokens[i + 1])

        if operator == "+":
            result += operand
        elif operator == "-":
            result -= operand
        elif operator == "*":
            result *= operand
        elif operator == "/":
            result //= operand

    return result
def solve(puzzle):
    unique_letters = extract_unique_letters(puzzle)
    if len(unique_letters) > 10:
        return None

    for perm in itertools.permutations(range(10), len(unique_letters)):
        if perm[unique_letters.index(puzzle[0])] == 0:
            continue

        trans = str.maketrans("".join(unique_letters), "".join(map(str, perm)))
        equation = puzzle.translate(trans).split(" == ")
        if evaluate_expression(equation[0]) == evaluate_expression(equation[1]):
            return int(equation[1])
    return None
