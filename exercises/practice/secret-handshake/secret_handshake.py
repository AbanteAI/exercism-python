def commands(binary_str):
def commands(binary_str):
    # Define the actions for each binary digit
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    reverse_order = False

    # Ensure the binary string is 5 characters long, padding with zeros if necessary
    binary_str = binary_str.zfill(5)

    # Check if we need to reverse the order of actions
    if binary_str[0] == '1':
        reverse_order = True

    # Convert the binary string to a list of actions
    # The rightmost digit of the binary string corresponds to the first action
    handshake_actions = [action for bit, action in zip(reversed(binary_str[1:]), actions) if bit == '1']

    # Reverse the order if the leftmost bit is 1
    if reverse_order:
        handshake_actions.reverse()

    return handshake_actions
