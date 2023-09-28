def saddle_points(matrix):
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    
    potential_trees = []
    for i, row in enumerate(matrix):
        max_value = max(row)
        for j, value in enumerate(row):
            if value == max_value:
                column = [matrix[k][j] for k in range(len(matrix))]
                if value == min(column):
                    potential_trees.append([i, j])
    
    return potential_trees
