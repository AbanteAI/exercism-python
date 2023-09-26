def rows(letter):
def rows(letter):
    diamond_size = ord(letter) - ord('A') + 1
    diamond = []
    if diamond_size == 1:
        return ["A"]
    for i in range(diamond_size):
        row = [' '] * diamond_size
        row[diamond_size // 2 - i] = chr(ord('A') + i)
        row[diamond_size // 2 + i] = chr(ord('A') + i)
        diamond.append(''.join(row))
    for i in range(diamond_size - 2, -1, -1):
        diamond.append(diamond[i])
    return diamond
        diamond.append(''.join(row))
    for i in range(diamond_size - 2, -1, -1):
        diamond.append(diamond[i])
    return diamond