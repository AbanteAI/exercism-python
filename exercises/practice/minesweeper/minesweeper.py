def annotate(minefield):
    if not minefield:
        return minefield

    rows = len(minefield)
    cols = len(minefield[0])

    # Check for invalid input
    for row in minefield:
        if len(row) != cols:
            raise ValueError("The board is invalid with current input.")
        for cell in row:
            if cell not in (' ', '*'):
                raise ValueError("The board is invalid with current input.")

    def count_adjacent_mines(r, c):
        count = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and minefield[nr][nc] == '*':
                    count += 1
        return count

    result = []
    for r in range(rows):
        row = []
        for c in range(cols):
            if minefield[r][c] == '*':
                row.append('*')
            else:
                count = count_adjacent_mines(r, c)
                row.append(str(count) if count > 0 else ' ')
        result.append(''.join(row))
    return result
