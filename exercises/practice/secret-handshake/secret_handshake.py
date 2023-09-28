def commands(binary_str):
    binary_num = int(binary_str, 2)
    actions = []
    
    if binary_num & 1:
        actions.append("wink")
    if binary_num & 2:
        actions.append("double blink")
    if binary_num & 4:
        actions.append("close your eyes")
    if binary_num & 8:
        actions.append("jump")
    if binary_num & 16:
        actions.reverse()

    return actions