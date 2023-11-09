def spiral_matrix(size):
    if size <= 0:
        return []

    # Initialize the matrix with zeros
    matrix = [[0] * size for _ in range(size)]

    # Define the initial boundaries of the spiral
    left, right, top, bottom = 0, size - 1, 0, size - 1
    num = 1  # Start with 1

    while left <= right and top <= bottom:
        # Traverse from left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Traverse downwards
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Traverse from right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # Traverse upwards
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix
