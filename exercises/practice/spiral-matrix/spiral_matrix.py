def spiral_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0
    current_number = 1
    current_row = 0
    current_col = 0

    for _ in range(size * size):
        matrix[current_row][current_col] = current_number
        current_number += 1

        next_row = current_row + directions[current_direction][0]
        next_col = current_col + directions[current_direction][1]

        if (
            next_row < 0
            or next_row >= size
            or next_col < 0
            or next_col >= size
            or matrix[next_row][next_col] != 0
        ):
            current_direction = (current_direction + 1) % 4

        current_row += directions[current_direction][0]
        current_col += directions[current_direction][1]

    return matrix
