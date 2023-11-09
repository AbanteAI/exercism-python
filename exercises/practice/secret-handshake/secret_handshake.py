def commands(binary_str):
    # Define the actions for each binary digit
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    result = []

    # Convert the binary string to a list of actions
    for i, digit in enumerate(reversed(binary_str[:5])):
        if digit == '1' and i < len(actions):
            result.append(actions[i])

    # If the binary string has a '1' in the leftmost place, reverse the result
    if len(binary_str) == 5 and binary_str[0] == '1':
        result.reverse()

    return result
