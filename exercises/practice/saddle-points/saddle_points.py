def saddle_points(matrix):
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    
    row_max = [max(row) for row in matrix]
    col_min = [min(col) for col in zip(*matrix)]

    result = []
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == row_max[i] and element == col_min[j]:
                result.append({"row": i + 1, "column": j + 1})

    return result