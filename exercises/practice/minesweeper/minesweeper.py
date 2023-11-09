def annotate(minefield):
    if not all(len(row) == len(minefield[0]) for row in minefield):
        raise ValueError("The board is invalid with current input.")
    if any(char not in (' ', '*') for row in minefield for char in row):
        raise ValueError("The board is invalid with current input.")

    def mine_count(x, y):
        count = 0
        for i in range(max(0, x-1), min(x+2, len(minefield))):
            for j in range(max(0, y-1), min(y+2, len(minefield[0]))):
                if minefield[i][j] == '*':
                    count += 1
        return count

    annotated_board = []
    for x, row in enumerate(minefield):
        annotated_row = ''
        for y, square in enumerate(row):
            if square == '*':
                annotated_row += '*'
            else:
                count = mine_count(x, y)
                annotated_row += str(count) if count > 0 else ' '
        annotated_board.append(annotated_row)
    
    return annotated_board
