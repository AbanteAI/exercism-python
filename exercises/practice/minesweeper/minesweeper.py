def annotate(minefield):
    validate_minefield(minefield)
    annotated_minefield = []
    for row in range(len(minefield)):
        annotated_row = []
        for col in range(len(minefield[row])):
            cell = minefield[row][col]
            if cell == '*':
                annotated_row.append('*')
            else:
                mines_around = count_mines_around(minefield, row, col)
                if mines_around > 0:
                    annotated_row.append(str(mines_around))
                else:
                    annotated_row.append(' ')
        annotated_minefield.append(annotated_row)

    return [''.join(row) for row in annotated_minefield]

def count_mines_around(minefield, row, col):
    rows = len(minefield)
    cols = len(minefield[0])
    count = 0

    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < rows and 0 <= c < cols and minefield[r][c] == '*':
                count += 1

    return count
def validate_minefield(minefield):
    if not minefield:
        return

    row_len = len(minefield[0])
    for row in minefield:
        if len(row) != row_len:
            raise ValueError("The board is invalid with current input.")

        for cell in row:
            if cell not in ['*', ' ']:
                raise ValueError("The board is invalid with current input.")