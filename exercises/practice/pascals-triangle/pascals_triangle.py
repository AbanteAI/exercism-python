def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    triangle = []

    for i in range(row_count):
        row = [1] * (i + 1)
        if i > 1:
        for j in range(1, i+1):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle