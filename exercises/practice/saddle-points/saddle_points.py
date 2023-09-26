    if not matrix:
        return set()
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    max_in_row = [max(row) for row in matrix]
    min_in_col = [min(col) for col in zip(*matrix)]
    
    saddle_points = set()
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == max_in_row[i] and matrix[i][j] == min_in_col[j]:
                saddle_points.add((i, j))
    
    return saddle_points
        return set()
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    max_in_row = [max(row) for row in matrix]
    min_in_col = [min(col) for col in zip(*matrix)]
    
    saddle_points = set()
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == max_in_row[i] and matrix[i][j] == min_in_col[j]:
                saddle_points.add((i, j))
    
    return saddle_points
