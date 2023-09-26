    rows = len(minefield)
    cols = len(minefield[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    def count_adjacent_mines(row, col):
        count = 0
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < rows and 0 <= new_col < cols and minefield[new_row][new_col] == '*':
                count += 1
        return count

    new_minefield = [list(row) for row in minefield]

    for row in range(rows):
        for col in range(cols):
            if new_minefield[row][col] == ' ':
                mine_count = count_adjacent_mines(row, col)
                if mine_count > 0:
                    new_minefield[row][col] = str(mine_count)

    return ["".join(row) for row in new_minefield]
