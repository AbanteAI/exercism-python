def saddle_points(matrix):
    if not matrix:
        return []

    # Check if the matrix is irregular
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("irregular matrix")

    # Find saddle points
    saddle_points_list = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == max(row) and value == min(column[j] for column in matrix):
                saddle_points_list.append({"row": i + 1, "column": j + 1})

    return saddle_points_list
