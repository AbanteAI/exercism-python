def spiral_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0
    row, col = 0, 0

    for num in range(1, size * size + 1):
        matrix[row][col] = num
        next_row = row + directions[direction_index][0]
        next_col = col + directions[direction_index][1]
        if (
            next_row < 0
            or next_row >= size
            or next_col < 0
            or next_col >= size
            or matrix[next_row][next_col] != 0
        ):
            direction_index = (direction_index + 1) % 4
            next_row = row + directions[direction_index][0]
            next_col = col + directions[direction_index][1]
        row, col = next_row, next_col

    return matrix