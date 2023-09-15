def rows(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    diamond = []
    index = alphabet.index(letter)

    for i in range(index + 1):
        if i == 0:
            row = " " * (index - i) + alphabet[i] + " " * (index - i)
        else:
            row = " " * (index - i) + alphabet[i] + " " * (2 * i - 1) + alphabet[i] + " " * (index - i)
        diamond.append(row)

    for i in range(index - 1, -1, -1):
        if i == 0:
            row = " " * (index - i) + alphabet[i] + " " * (index - i)
        else:
            row = " " * (index - i) + alphabet[i] + " " * (2 * i - 1) + alphabet[i] + " " * (index - i)
        diamond.append(row)

    return diamond