def commands(binary_str):
    # Define the actions for each binary digit
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    # Convert the binary string to a list of actions
    result = [action for bit, action in zip(binary_str[::-1], actions) if bit == '1']
    # Check if we need to reverse the actions
    if len(binary_str) == 5 and binary_str[0] == '1':
        result.reverse()
    return result