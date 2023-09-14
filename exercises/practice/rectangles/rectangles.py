def rectangles(strings):
    count = 0
    for y in range(len(strings)):
        for x in range(len(strings[y])):
            if strings[y][x] == "+":
                for row in range(y + 1, len(strings)):
                    if strings[row][x] == "+":
                        for col in range(x + 1, len(strings[y])):
                            if strings[y][col] == "+" and strings[row][col] == "+":
                                if all(c in "+|" for c in (strings[y][i] for i in range(x + 1, col))) and \
                                   all(c in "+-" for c in (strings[i][x] for i in range(y + 1, row))) and \
                                   all(c in "+|" for c in (strings[row][i] for i in range(x + 1, col))) and \
                                   all(c in "+-" for c in (strings[i][col] for i in range(y + 1, row))):
                                    count += 1
    return count