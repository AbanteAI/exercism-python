def rectangles(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            if strings[i][j] == "+":
                count += 1
                x, y = i, j
                while x < len(strings) and strings[x][j] == "|":
                    x += 1
                while y < len(strings[i]) and strings[i][y] == "-":
                    y += 1
                for k in range(i, x):
                    for l in range(j, y):
                        if strings[k][l] != "+" and strings[k][l] != "|" and strings[k][l] != "-":
                            return -1
    return count
