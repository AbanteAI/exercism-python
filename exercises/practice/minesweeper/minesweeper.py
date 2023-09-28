def annotate(minefield):
    def count_adjacent_mines(row, col):
        return sum(1 for r in range(row - 1, row + 2)
                   for c in range(col - 1, col + 2)
                   if 0 <= r < len(minefield) and 0 <= c < len(minefield[0]) and minefield[r][c] == "*")

    if not minefield:
    if len(set(map(len, minefield))) != 1:
        raise ValueError("The board is invalid with current input.")
        return minefield

    for row in minefield:
        if not all(c in " *"
                   for c in row):
            raise ValueError("The board is invalid with current input.")

    annotated_minefield = []
    for row in range(len(minefield)):
        annotated_row = ''
        for col in range(len(minefield[0])):
            if minefield[row][col] == "*":
                annotated_row += "*"
            else:
                adjacent_mines = count_adjacent_mines(row, col)
                annotated_row += str(adjacent_mines) if adjacent_mines > 0 else " "
        annotated_minefield.append(annotated_row)

    return annotated_minefield