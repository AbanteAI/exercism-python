def annotate(minefield):
    if not minefield:
        return []

    rows = len(minefield)
    cols = len(minefield[0])

    def count_adjacent_mines(row, col):
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < rows and 0 <= j < cols and minefield[i][j] == '*':
                    count += 1
        return count

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if minefield[i][j] == ' ':
                count = count_adjacent_mines(i, j)
                row.append(str(count) if count > 0 else ' ')
            elif minefield[i][j] == '*':
                row.append('*')
            else:
                raise ValueError("Invalid character in minefield")
        result.append(''.join(row))
    return result

    def count_adjacent_mines(row, col):
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < rows and 0 <= j < cols and minefield[i][j] == '*':
                    count += 1
        return count

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if minefield[i][j] == ' ':
                count = count_adjacent_mines(i, j)
                row.append(str(count) if count > 0 else ' ')
            else:
                row.append(minefield[i][j])
        result.append(''.join(row))
    return result
