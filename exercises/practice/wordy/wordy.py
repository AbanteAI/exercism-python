def answer(question):
    question = question.replace('?', '').replace('by', '')
    words = question.split()
    if words[0] != 'What' or words[1] != 'is':
        raise ValueError("syntax error")

    try:
        result = int(words[2])
    except ValueError:
        raise ValueError("syntax error")

    i = 3
    while i < len(words):
        operator = words[i]
        if operator not in ['plus', 'minus', 'multiplied', 'divided']:
            raise ValueError("unknown operation")

        try:
            num = int(words[i + 1])
        except ValueError:
            raise ValueError("syntax error")

        if operator == 'plus':
            result += num
        elif operator == 'minus':
            result -= num
        elif operator == 'multiplied':
            result *= num
        elif operator == 'divided':
            result /= num

        i += 2

    return result
