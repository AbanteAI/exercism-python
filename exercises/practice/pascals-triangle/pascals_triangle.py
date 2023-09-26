def rows(row_count):
    if row_count <= 0:
        raise ValueError("row_count must be a positive integer")

    triangle = []
    for i in range(row_count):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle