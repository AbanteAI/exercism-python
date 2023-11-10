def answer(question):
    # Check if the question starts with 'What is' and ends with '?'
    if not question.startswith('What is ') or not question.endswith('?'):
        raise ValueError("syntax error")

    # Remove question mark and 'What is ' part of the question
    question = question[:-1].replace('What is ', '')

    # Split the question into parts
    parts = question.split()

    # Initialize the result and the current operation
    result = None
    operation = None

    # Iterate over the parts of the question
    for part in parts:
        if part.isdigit() or (part.startswith('-') and part[1:].isdigit()):
            # Convert number strings to integers
            number = int(part)
            if result is None:
                # If no result yet, set the result to the current number
                result = number
            elif operation is not None:
                # Perform the operation with the current number
                if operation == 'plus':
                    result += number
                elif operation == 'minus':
                    result -= number
                elif operation == 'multiplied':
                    result *= number
                elif operation == 'divided':
                    result //= number
                operation = None  # Reset the operation after using it
            else:
                # If there is a number but no operation, raise an error
                raise ValueError("syntax error")
        else:
            # If the part is not a number, it should be an operation
            if part in ['plus', 'minus', 'multiplied', 'divided']:
                if operation is not None:
                    # If there is already an operation, raise an error
                    raise ValueError("syntax error")
                operation = part
            elif part == 'by':
                # 'by' is part of 'multiplied by' and 'divided by'
                continue
            else:
                # If the part is not an operation or 'by', raise an error
                raise ValueError("unknown operation")

    if result is None or operation is not None:
        # If there is no result or there is an operation without a number, raise an error
        raise ValueError("syntax error")

    return result