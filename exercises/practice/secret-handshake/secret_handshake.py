def commands(binary_str):
    actions = ["wink", "double blink", "close your eyes", "jump"]
    binary_num = int(binary_str, 2)
    result = [actions[i] for i in range(4) if binary_num & (1 << i)]
    if binary_num & (1 << 4):
        result.reverse()
    return result