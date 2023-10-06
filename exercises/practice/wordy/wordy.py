import re

def answer(question):
    question = question.replace("What is ", "").replace("?", "")
    operations = {
        "plus": lambda x, y: x + y,
        "minus": lambda x, y: x - y,
        "multiplied by": lambda x, y: x * y,
        "divided by": lambda x, y: x // y,
    }
    
    tokens = re.split(r" (plus|minus|multiplied by|divided by) ", question)
    if len(tokens) == 1:
        try:
            return int(tokens[0])
        except ValueError:
            pass
    elif len(tokens) < 2:
    
    try:
        result = int(tokens[0])
    except ValueError:
        raise ValueError("unknown operation")
    for i in range(1, len(tokens)-1, 2):
        operation = tokens[i]
        try:
            number = int(tokens[i+1])
        except ValueError:
            raise ValueError("syntax error")
        
        if operation not in operations:
            raise ValueError("unknown operation")
        
        result = operations[operation](result, number)
    
    return result