def rows(letter):
    if letter == "A":
        return ["A"]
    
    n = ord(letter) - ord("A") + 1
    diamond = []
    
    for i in range(n):
        spaces = " " * (n - i - 1)
        if i == 0:
            line = spaces + "A" + spaces
        else:
            line = spaces + chr(ord("A") + i) + " " * (2 * i - 1) + chr(ord("A") + i) + spaces
        diamond.append(line)
    
    for i in range(n - 2, -1, -1):
        diamond.append(diamond[i])
    
    return diamond