def spiral_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    count = 1
    for layer in range((size + 1) // 2):
        for i in range(layer, size - layer):  # Traverse right
            matrix[layer][i] = count
            count += 1
        for i in range(layer + 1, size - layer):  # Traverse down
            matrix[i][size - layer - 1] = count
            count += 1
        for i in range(layer + 1, size - layer):  # Traverse left
            matrix[size - layer - 1][size - i - 1] = count
            count += 1
        for i in range(layer + 1, size - layer - 1):  # Traverse up
            matrix[size - i - 1][layer] = count
            count += 1
    return matrix