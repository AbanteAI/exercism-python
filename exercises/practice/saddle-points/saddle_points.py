def saddle_points(matrix):
    if not matrix:
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Irregular matrix")
        return []

    row_maxes = [max(row) for row in matrix]
    col_mins = [min(col) for col in zip(*matrix)]

    result = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == row_maxes[i] and value == col_mins[j]:
                result.append({"row": i + 1, "column": j + 1})

    return result
