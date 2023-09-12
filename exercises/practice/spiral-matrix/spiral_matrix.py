def spiral_matrix(size):
    if size == 0:
        return []

    matrix = [[0] * size for _ in range(size)]
    num = 1
    for layer in range((size + 1) // 2):
        for i in range(layer, size - layer):
            matrix[layer][i] = num
            num += 1
        for i in range(layer + 1, size - layer):
            matrix[i][size - layer - 1] = num
            num += 1
        for i in range(layer + 1, size - layer):
            matrix[size - layer - 1][size - i - 1] = num
            num += 1
        for i in range(layer + 1, size - layer - 1):
            matrix[size - i - 1][layer] = num
            num += 1
    return matrix