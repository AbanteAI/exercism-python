def rows(letter):
    if not letter.isalpha() or not letter.isupper():
        raise ValueError("Input must be an uppercase letter.")

    size = ord(letter) - ord('A') + 1
    diamond = []

    for i in range(size):
        row = ' ' * (size - i - 1) + chr(ord('A') + i)
        if i > 0:
            row += ' ' * (2 * i - 1) + chr(ord('A') + i)
        row += ' ' * (size - i - 1)
        diamond.append(row)

    for i in range(size - 2, -1, -1):
        diamond.append(diamond[i])

    return diamond