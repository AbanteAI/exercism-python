def annotate(minefield):
    if not all(len(row) == len(minefield[0]) for row in minefield) or any(char not in (' ', '*') for row in minefield for char in row):
        raise ValueError("The board is invalid with current input.")
    if not minefield:
        return []

    def get_mine_count(x, y):
        count = 0
        for i in range(max(0, x-1), min(x+2, len(minefield))):
            for j in range(max(0, y-1), min(y+2, len(minefield[0]))):
                if minefield[i][j] == '*':
                    count += 1
        return count

    annotated = []
    for x, row in enumerate(minefield):
        new_row = ''
        for y, cell in enumerate(row):
            if cell == '*':
                new_row += '*'
            else:
                mine_count = get_mine_count(x, y)
                new_row += str(mine_count) if mine_count > 0 else ' '
        annotated.append(new_row)

    return annotated