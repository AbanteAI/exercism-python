def rows(letter):
    diamond = []
    size = ord(letter) - ord('A') + 1
    width = 2 * size - 1

    for i in range(size):
        row = [' '] * width
        row[size - i - 1] = chr(ord('A') + i)
        row[size + i - 1] = chr(ord('A') + i)
        diamond.append(''.join(row))

    for i in range(size - 2, -1, -1):
        diamond.append(diamond[i])

    return diamond
