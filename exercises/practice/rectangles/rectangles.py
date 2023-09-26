def rectangles(strings):
    count = 0
    if not strings:
        return count

    rows = len(strings)
    cols = len(strings[0])

    for i in range(rows):
        for j in range(cols):
            if strings[i][j] == '+':
                for k in range(i + 1, rows):
                    if strings[k][j] == '+':
                        for l in range(j + 1, cols):
                            if strings[i][l] == '+' and strings[k][l] == '+':
                                count += 1
                            else:
                                break
                    else:
                        break

    return count
    if not strings:
        return count

    rows = len(strings)
    cols = len(strings[0])

    for i in range(rows):
        for j in range(cols):
            if strings[i][j] == '+':
                for k in range(i + 1, rows):
                    if strings[k][j] == '+':
                        for l in range(j + 1, cols):
                            if strings[i][l] == '+' and strings[k][l] == '+':
                                count += 1
                            else:
                                break
                    else:
                        break

    return count
