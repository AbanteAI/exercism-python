def annotate(minefield):
    if not all(len(row) == len(minefield[0]) for row in minefield):
        raise ValueError("The board is invalid with current input.")
    
    if any(char not in (' ', '*') for row in minefield for char in row):
        raise ValueError("The board is invalid with current input.")
    def mine_at(i, j):
        if i < 0 or i >= len(minefield) or j < 0 or j >= len(minefield[0]):
            return 0
        return 1 if minefield[i][j] == '*' else 0

    def adjacent_mines_count(i, j):
        return sum(mine_at(i + x, j + y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0))

    annotated_board = []
    for i, row in enumerate(minefield):
        annotated_row = ''
        for j, square in enumerate(row):
            if square == '*':
                annotated_row += '*'
            else:
                count = adjacent_mines_count(i, j)
                annotated_row += str(count) if count > 0 else ' '
        annotated_board.append(annotated_row)
    
    return annotated_board