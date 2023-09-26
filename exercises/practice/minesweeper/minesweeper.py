def annotate(minefield):
    if len(minefield) == 0 or len(minefield[0]) == 0:
        return minefield

    rows = len(minefield)
    cols = len(minefield[0])

    def count_adjacent_mines(row, col):
        count = 0
        for i in range(max(0, row - 1), min(row + 2, rows)):
            for j in range(max(0, col - 1), min(col + 2, cols)):
                if minefield[i][j] == "*" and (i != row or j != col):
                    count += 1
        return count

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if minefield[i][j] == " ":
                count = count_adjacent_mines(i, j)
                if count > 0:
                    row.append(str(count))
                else:
                    row.append(" ")
            elif minefield[i][j] == "*":
                row.append("*")
            else:
                raise ValueError("Invalid character in minefield")
        result.append("".join(row))
    return result
    cols = len(minefield[0])

    def count_adjacent_mines(row, col):
        count = 0
        for i in range(max(0, row - 1), min(row + 2, rows)):
            for j in range(max(0, col - 1), min(col + 2, cols)):
                if minefield[i][j] == "*" and (i != row or j != col):
                    count += 1
        return count

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if minefield[i][j] == " ":
                count = count_adjacent_mines(i, j)
                if count > 0:
                    row.append(str(count))
                else:
                    row.append(" ")
            else:
                row.append(minefield[i][j])
        result.append("".join(row))
    return result
