def commands(binary_str):
    actions = []
    binary_len = len(binary_str)

    if binary_len >= 1 and binary_str[-1] == "1":
        actions.append("wink")
    if binary_len >= 2 and binary_str[-2] == "1":
        actions.append("double blink")
    if binary_len >= 3 and binary_str[-3] == "1":
        actions.append("close your eyes")
    if binary_len >= 4 and binary_str[-4] == "1":
        actions.append("jump")
    if binary_len >= 5 and binary_str[-5] == "1":
        actions.reverse()

    return actions
    actions = []
    binary_len = len(binary_str)

    if binary_len >= 1 and binary_str[-1] == "1":
        actions.append("wink")
    if binary_len >= 2 and binary_str[-2] == "1":
        actions.append("double blink")
    if binary_len >= 3 and binary_str[-3] == "1":
        actions.append("close your eyes")
    if binary_len >= 4 and binary_str[-4] == "1":
        actions.append("jump")
    if binary_len >= 5 and binary_str[-5] == "1":
        actions.reverse()

    return actions
