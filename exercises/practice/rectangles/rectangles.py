def rectangles(strings):
    count = 0

    if not strings or not strings[0]:
        return count

    rows = len(strings)
    cols = len(strings[0])

    for i in range(rows):
        for j in range(cols):
            if strings[i][j] == "+":
                count += count_rectangles(strings, i, j)

    return count


def count_rectangles(strings, start_row, start_col):
    rows = len(strings)
    cols = len(strings[0])
    count = 0

    for i in range(start_row + 1, rows):
        if strings[i][start_col] == "+":
            for j in range(start_col + 1, cols):
                if strings[i][j] == "+":
                    if all(strings[k][j] == "+" for k in range(start_row, i + 1)):
                        count += 1
                else:
                    break
        else:
            break

    return count