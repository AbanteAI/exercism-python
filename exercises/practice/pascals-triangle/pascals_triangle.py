def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")

    triangle = [[1] * (i + 1) for i in range(row_count)]
    for i in range(2, row_count):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle