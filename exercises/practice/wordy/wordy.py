def answer(question):
    words = question.split()
    if words[0] != 'What' or words[-1] != '?':
        raise ValueError("syntax error: Invalid question format")

    i = 2
    result = int(words[2])
    while i < len(words) - 1:
        if words[i] == 'plus':
            result += int(words[i+1])
        elif words[i] == 'minus':
            result -= int(words[i+1])
        elif words[i] == 'multiplied' and words[i+1] == 'by':
            result *= int(words[i+2])
            i += 1
        elif words[i] == 'divided' and words[i+1] == 'by':
            result /= int(words[i+2])
            i += 1
        else:
            raise ValueError("unknown operation")
        i += 2

    return result
