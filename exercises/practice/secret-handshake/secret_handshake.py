def commands(binary_str):
    actions = {
        '00001': 'wink',
        '00010': 'double blink',
        '00100': 'close your eyes',
        '01000': 'jump',
        '10000': 'reverse actions'
    }

    handshake = []
    binary_str = binary_str[::-1]  # Reverse the binary string

    for i, digit in enumerate(binary_str):
        if i < 5 and digit == '1':
            action = actions.get('1' + '0' * i)  # Get the corresponding action
            if action:
                handshake.append(action)

    if len(binary_str) >= 5 and binary_str[4] == '1':  # Check if reverse actions is requested
        handshake.reverse()

    return handshake
        handshake.reverse()

    return handshake
