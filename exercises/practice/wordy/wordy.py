import re

def answer(question):
    # Remove question mark and 'What is ' part
    question = question.replace('?', '').replace('What is ', '', 1)

    # Define the operations
    operations = {
        'plus': '+',
        'minus': '-',
        'multiplied by': '*',
        'divided by': '/'
    }

    # Replace words with actual operators
    for word, operator in operations.items():
        question = question.replace(word, operator)

    # Check for unsupported operations
    if re.search(r'cubed|to the power of', question):
        raise ValueError("unknown operation")

    # Check for non-math questions
    if re.search(r'Who|What|When|Where|Why|How', question):
        raise ValueError("unknown operation")

    # Check for invalid syntax
    if not re.fullmatch(r'(-?\d+)( (plus|minus|multiplied by|divided by) -?\d+)*', question):
        raise ValueError("syntax error")

    # Split the question into parts
    parts = re.findall(r'-?\d+|plus|minus|multiplied by|divided by', question)

    # Evaluate the expression from left-to-right
    result = int(parts[0])
    for i in range(1, len(parts) - 1, 2):
        operator = parts[i]
        value = int(parts[i + 1])
        if operator == 'plus':
            result += value
        elif operator == 'minus':
            result -= value
        elif operator == 'multiplied by':
            result *= value
        elif operator == 'divided by':
            result //= value

    return result