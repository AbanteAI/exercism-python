def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")

    triangle = []
    for i in range(row_count):
        row = [1] * (i + 1)
        for j in range(1, i + 1):
        triangle.append(row)
    return triangle
