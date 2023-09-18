def saddle_points(matrix):
    if not matrix:
        return set()

    result = set()
    for i, row in enumerate(matrix):
        max_row_value = max(row)
        for j, value in enumerate(row):
            if value == max_row_value:
                min_col_value = min([matrix[k][j] for k in range(len(matrix))])
                if value == min_col_value:
                    result.add((i+1, j+1))

    return result