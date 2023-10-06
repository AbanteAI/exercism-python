def rectangles(strings):
    count = 0
    rows = len(strings)
    cols = len(strings[0])
    for i in range(rows):
        for j in range(cols):
            if strings[i][j] == '+':
                for k in range(i + 1, rows):
                    if strings[k][j] == '+':
                        for l in range(j + 1, cols):
                            if strings[i][l] == '+' and strings[k][l] == '+':
                                valid_rectangle = True
                                for m in range(i + 1, k):
                                    if strings[m][l] not in ['+', '|']:
                                        valid_rectangle = False
                                        break
                                if valid_rectangle:
                                    count += 1
                            else:
                                break
                    else:
                        break
                    else:
                        break
    return count
