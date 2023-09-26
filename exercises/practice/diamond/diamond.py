def rows(letter):
    size = ord(letter) - ord('A') + 1
    diamond = []

    for i in range(size):
        row = [' '] * (2 * size - 1)
        row[size - 1 - i] = row[size - 1 + i] = chr(ord('A') + i)
        diamond.append(''.join(row))

    for i in range(size - 2, -1, -1):
        diamond.append(diamond[i])

    return diamond
