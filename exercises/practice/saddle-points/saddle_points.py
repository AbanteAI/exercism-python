def saddle_points(matrix):
    if not matrix:
        if any(len(row) != len(matrix[0]) for row in matrix):
            raise ValueError("Irregular matrix")
        return set()

    row_max = [max(row) for row in matrix]
    col_min = [min(col) for col in zip(*matrix)]

    saddle = set()
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == row_max[i] and value == col_min[j]:
                saddle.add((i, j))

    return saddle