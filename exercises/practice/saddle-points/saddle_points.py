def saddle_points(matrix):
    if not matrix:
        return []

    # Check if the matrix is irregular
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    # Find saddle points
    saddle_points_list = []
    for i, row in enumerate(matrix):
        row_max = max(row)
        for j, value in enumerate(row):
            if value == row_max and all(value <= matrix[k][j] for k in range(len(matrix))):
                saddle_points_list.append({"row": i + 1, "column": j + 1})

    return saddle_points_list
