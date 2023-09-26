def saddle_points(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    max_in_rows = [max(row) for row in matrix]
    min_in_cols = [min([matrix[i][j] for i in range(rows)]) for j in range(cols)]

    return [{"row": i + 1, "column": j + 1} for i, j in saddle_points]
