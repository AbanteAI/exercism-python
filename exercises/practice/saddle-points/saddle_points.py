def saddle_points(matrix):
    if not matrix:
        return []

    # Check if the matrix is irregular
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("irregular matrix")

    # Find the largest values in each row
    largest_row_values = [max(row) for row in matrix]

    # Find the smallest values in each column
    smallest_col_values = [min(col) for col in zip(*matrix)]

    # Find the intersection of the largest row values and smallest column values
    intersection = [
        {"row": i + 1, "column": j + 1}
        for i, row_max in enumerate(largest_row_values)
        for j, col_min in enumerate(smallest_col_values)
        if matrix[i][j] == row_max == col_min
    ]

    return intersection