def rectangles(strings):
    count = 0
    for i in range(len(strings) - 1):
        for j in range(len(strings[i]) - 1):
            if strings[i][j] == '+':
                for k in range(i + 1, len(strings)):
                    if strings[k][j] == '+':
                        for l in range(j + 1, len(strings[i])):
                            if strings[i][l] == '+':
                                if all(strings[m][l] == '+' for m in range(i + 1, k)):
                                    count += 1
                                else:
                                    break
                            else:
                                break
                    else:
                        break
    return count
