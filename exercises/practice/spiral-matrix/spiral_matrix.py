def spiral_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    row, col = 0, 0
    direction = 'right'
    for num in range(1, size * size + 1):
        matrix[row][col] = num
        if direction == 'right':
            if col + 1 == size or matrix[row][col + 1] != 0:
                direction = 'down'
                row += 1
            else:
                col += 1
        elif direction == 'down':
            if row + 1 == size or matrix[row + 1][col] != 0:
                direction = 'left'
                col -= 1
            else:
                row += 1
        elif direction == 'left':
            if col == 0 or matrix[row][col - 1] != 0:
                direction = 'up'
                row -= 1
            else:
                col -= 1
        elif direction == 'up':
            if row == 0 or matrix[row - 1][col] != 0:
                direction = 'right'
                col += 1
            else:
                row -= 1
    return matrix
