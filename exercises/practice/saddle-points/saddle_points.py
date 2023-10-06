def saddle_points(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    if any(len(row) != cols for row in matrix):
        raise ValueError("Irregular matrix")

    saddle_points = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == max(matrix[i]) and matrix[i][j] == min(matrix[k][j] for k in range(rows)):
                saddle_points.append({"row": i + 1, "column": j + 1})

    return saddle_points