def saddle_points(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    saddle_points = []
    for i in range(rows):
        for j in range(cols):
            if all(matrix[i][j] >= matrix[i][k] for k in range(cols)) and all(matrix[i][j] <= matrix[k][j] for k in range(rows)):
                saddle_points.append((i, j))

    if any(len(row) != cols for row in matrix):
        raise ValueError("irregular matrix")
