def rows(letter):
    n = ord(letter) - ord("A") + 1
    diamond = []

    for i in range(n):
        row = [" "] * (2 * n - 1)
        row[n - i - 1] = chr(ord("A") + i)
        row[n + i - 1] = chr(ord("A") + i)
        diamond.append("".join(row))

    for i in range(n - 2, -1, -1):
        diamond.append(diamond[i])

    return diamond