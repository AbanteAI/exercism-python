def commands(binary_str):
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    result = []
    binary_int = int(binary_str, 2)

    for i in range(4):
        if binary_int & (1 << i):
            result.append(actions[i])

    if binary_int & (1 << 4):
        result.reverse()

    return result
