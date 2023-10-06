def spiral_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0
    current_position = (0, 0)
    for num in range(1, size * size + 1):
        matrix[current_position[0]][current_position[1]] = num
        next_position = (current_position[0] + directions[current_direction][0],
                         current_position[1] + directions[current_direction][1])
        if not (0 <= next_position[0] < size and 0 <= next_position[1] < size) or matrix[next_position[0]][next_position[1]] != 0:
            current_direction = (current_direction + 1) % 4
            next_position = (current_position[0] + directions[current_direction][0],
                             current_position[1] + directions[current_direction][1])
        current_position = next_position
    return matrix
