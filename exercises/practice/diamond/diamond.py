def rows(letter):
    if letter == "A":
        return ["A"]

    diamond = []
    size = ord(letter) - ord("A") + 1
    width = size * 2 - 1

for i in range(size):
    row = [" "] * width
    char = chr(ord("A") + i)
    row[size - i - 1] = char
    row[size + i - 1] = char
    diamond.append("".join(row))

for i in range(size - 2, -1, -1):
    diamond.append(diamond[i])

    return diamond