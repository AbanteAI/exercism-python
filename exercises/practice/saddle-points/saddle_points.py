def saddle_points(matrix):
    if not matrix:
        return []

    # Check for irregular matrix
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("irregular matrix")

    # Find saddle points
    saddle_points_list = []
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == max(row) and cell == min([matrix[k][j] for k in range(len(matrix))]):
                saddle_points_list.append({"row": i + 1, "column": j + 1})

    return saddle_points_list
