import re

def answer(question):
    # Remove the question mark and the 'What is' part of the question
    question = question.replace('?', '').replace('What is ', '')

def answer(question):
    # Remove the question mark and the 'What is' part of the question
    question = question.replace('?', '').replace('What is ', '')

    # Define a pattern to match numbers and words for operations
    # The pattern now correctly captures negative numbers
    pattern = re.compile(r'(-?\d+|plus|minus|multiplied by|divided by)')
    tokens = pattern.findall(question)

    # Check if the question is malformed or contains unknown operations
    # Improved error checking for unknown operations and malformed questions
    if not tokens or 'by' in tokens:
        raise ValueError("syntax error")

    # Initialize the result with the first number
    result = int(tokens[0])

    # Iterate over the tokens and evaluate the expression
    i = 1
    while i < len(tokens):
        operation = tokens[i]
        if operation not in ('plus', 'minus', 'multiplied by', 'divided by'):
            raise ValueError("unknown operation")

        if i + 2 < len(tokens) and tokens[i + 1] == 'by':
            operation += ' ' + tokens[i + 1]
            i += 1

        if i + 1 < len(tokens):
            number = int(tokens[i + 1])
            if operation == 'plus':
                result += number
            elif operation == 'minus':
                result -= number
            elif operation == 'multiplied by':
                result *= number
            elif operation == 'divided by':
                if number == 0:
                    raise ValueError("division by zero")
                result //= number
            i += 2
        else:
            raise ValueError("syntax error")

    return result

    return result