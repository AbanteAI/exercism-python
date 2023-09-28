def annotate(minefield):
    board = [list(row) for row in minefield]
    rows = len(board)
    cols = len(board[0])
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '*':
                continue
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    ni = i + dx
                    nj = j + dy
                    if ni >= 0 and ni < rows and nj >= 0 and nj < cols and board[ni][nj] == '*':
                        count += 1
            board[i][j] = str(count)
    return [''.join(row) for row in board]
