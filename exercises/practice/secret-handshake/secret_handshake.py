def commands(binary_str):
    # Define the actions for each binary digit
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    handshake = []

    # Ensure the binary string is 5 characters long, padding with zeros if necessary
    binary_str = binary_str.zfill(5)

    # Check each binary digit and add the corresponding action
    for i, action in enumerate(actions):
        if binary_str[-i-1] == '1':
            handshake.append(action)

    # If the leftmost binary digit is '1', reverse the order of actions
    if binary_str[0] == '1':
        handshake.reverse()

    return handshake
