def rectangles(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            if strings[i][j] == "+":
                count += 1
                k = j + 1
                while k < len(strings[i]) and strings[i][k] == "-":
                    k += 1
                    if k < len(strings[i]) and strings[i][k] == "+":
                        l = i + 1
                        while l < len(strings) and strings[l][j] == "|":
                            l += 1
                            if l < len(strings) and strings[l][j] == "+":
                                count += 1
                            else:
                                break
                    else:
                        break
    return count
