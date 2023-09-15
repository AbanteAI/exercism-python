def commands(binary_str):
    actions = [
        ("wink", "00001"),
        ("double blink", "00010"),
        ("close your eyes", "00100"),
        ("jump", "01000"),
        ("reverse", "10000")
    ]
    
    binary_str = format(int(binary_str), '05b')
    result = []
    
    for i in range(len(binary_str) - 1, -1, -1):
        if binary_str[i] == "1":
            action, _ = actions[-i - 1]
            result.append(action)
    
    if "reverse" in result:
        result.remove("reverse")
        result.reverse()
    
    return result