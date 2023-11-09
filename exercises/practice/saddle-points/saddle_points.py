def saddle_points(matrix):
    if not matrix:
        return []

    # Check if the matrix is irregular
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    # Find all saddle points
    saddle_points_list = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == max(row) and value == min(col[j] for col in matrix):
                saddle_points_list.append({"row": i + 1, "column": j + 1})

    return saddle_points_list
