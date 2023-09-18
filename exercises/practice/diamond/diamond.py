def rows(letter):
    size = ord(letter) - ord('A') + 1
    diamond = []

    for i in range(size):
        row = [' '] * (size * 2 - 1)
        row[size - i - 1] = chr(ord('A') + i)
        row[size + i - 1] = chr(ord('A') + i)
        diamond.append(''.join(row))

    for i in range(size - 2, -1, -1):
        diamond.append(diamond[i])

    return diamond