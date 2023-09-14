def rows(letter):
    size = ord(letter) - ord('A') + 1
    result = []

    for i in range(size):
        row = [' '] * (2 * size - 1)
        row[size - i - 1] = row[size + i - 1] = chr(ord('A') + i)
        result.append(''.join(row))

    for i in range(size - 2, -1, -1):
        result.append(result[i])

    return result