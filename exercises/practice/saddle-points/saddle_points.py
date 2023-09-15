def saddle_points(matrix):
    saddle_points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            value = matrix[i][j]
            if value == max(matrix[i]) and value == min(row[j] for row in matrix):
                saddle_points.append((i, j))
    return saddle_points
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            value = matrix[i][j]
            if value == max(matrix[i]) and value == min(row[j] for row in matrix):
                saddle_points.append((i, j))
    return saddle_points
