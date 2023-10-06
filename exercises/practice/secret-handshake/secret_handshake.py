def commands(binary_str):
    actions = ["wink", "double blink", "close your eyes", "jump"]
    handshake = []
    
    for i, action in enumerate(actions):
        if binary_str[-(i+1)] == '1':
            handshake.append(action)
    
    if len(binary_str) == 5 and binary_str[0] == '1':
        handshake.reverse()
    
    return handshake
