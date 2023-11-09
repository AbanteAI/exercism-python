import re

def answer(question):
    # Remove the question mark and 'What is ' part
    question = question.replace('?', '').replace('What is ', '', 1)

    # Define the pattern for matching numbers and operators
    pattern = r'(-?\d+|plus|minus|multiplied by|divided by)'
    tokens = re.findall(pattern, question)
    # Check for unsupported operations and non-math questions
    if 'cubed' in question or not re.match(r'^(-?\d+ (plus|minus|multiplied by|divided by) )+-?\d+$', ' '.join(tokens)):
        raise ValueError("unknown operation")

    # Check for invalid syntax or unknown operations
    if not tokens or any(op in tokens[-1] for op in ['plus', 'minus', 'multiplied by', 'divided by']):
        raise ValueError("syntax error")

    # Initialize the result with the first number
    result = int(tokens[0])

    # Iterate over the tokens and perform the operations
    i = 1
    while i < len(tokens):
        if tokens[i] == 'plus':
            result += int(tokens[i+1])
        elif tokens[i] == 'minus':
            result -= int(tokens[i+1])
        elif tokens[i] == 'multiplied by':
            result *= int(tokens[i+1])
            result //= int(tokens[i+1]) if int(tokens[i+1]) > 0 else -(-result // int(tokens[i+1]))
        else:
            raise ValueError("unknown operation")
        i += 2

    return result
