def annotate(minefield):
    def count_mines(row, col):
        return sum(1 for r in range(row - 1, row + 2)
                   for c in range(col - 1, col + 2)
                   if 0 <= r < len(minefield) and 0 <= c < len(minefield[0]) and minefield[r][c] == '*')

    if len(set(len(row) for row in minefield)) > 1:
        raise ValueError("Rows have different lengths.")

    if any(char not in (' ', '*') for row in minefield for char in row):
        raise ValueError("Invalid character in minefield.")
    annotated_board = []
    for row in range(len(minefield)):
        annotated_row = ''
        for col in range(len(minefield[row])):
            if minefield[row][col] == '*':
                annotated_row += '*'
            else:
                mines = count_mines(row, col)
                annotated_row += str(mines) if mines > 0 else ' '
        annotated_board.append(annotated_row)
    return annotated_board