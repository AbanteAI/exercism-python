def spiral_matrix(size):
    if size < 1:
        return []

    # Initialize the matrix with zeros
    matrix = [[0] * size for _ in range(size)]

    # Define the directions for the spiral movement (right, down, left, up)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0  # Start with moving right

    # Starting position
    row, col = 0, 0

    for num in range(1, size * size + 1):
        matrix[row][col] = num  # Fill the cell with the current number

        # Calculate the next position
        next_row = row + directions[current_direction][0]
        next_col = col + directions[current_direction][1]

        # Check if the next position is within bounds and the cell is not yet filled
        if (0 <= next_row < size and 0 <= next_col < size and matrix[next_row][next_col] == 0):
            row, col = next_row, next_col
        else:
            # Change direction
            current_direction = (current_direction + 1) % 4
            row += directions[current_direction][0]
            col += directions[current_direction][1]

    return matrix