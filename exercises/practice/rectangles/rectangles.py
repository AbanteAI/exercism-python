def is_corner(grid, row, col):
    return grid[row][col] == '+' and (
        (row > 0 and grid[row - 1][col] in '|+') and
        (row < len(grid) - 1 and grid[row + 1][col] in '|+') and
        (col > 0 and grid[row][col - 1] in '-+') and
        (col < len(grid[row]) - 1 and grid[row][col + 1] in '-+')
    )

def is_horizontal_edge(grid, row, col1, col2):
    return all(grid[row][col] in '-+' for col in range(col1 + 1, col2))

def is_vertical_edge(grid, col, row1, row2):
    return all(grid[row][col] in '|+' for row in range(row1 + 1, row2))

def is_rectangle(grid, top_left, bottom_right):
    if not (is_corner(grid, *top_left) and is_corner(grid, *bottom_right)):
        return False
    top_right = (top_left[0], bottom_right[1])
    bottom_left = (bottom_right[0], top_left[1])
    if not (is_corner(grid, *top_right) and is_corner(grid, *bottom_left)):
        return False
    if not (is_horizontal_edge(grid, top_left[0], top_left[1], bottom_right[1]) and
            is_horizontal_edge(grid, bottom_right[0], top_left[1], bottom_right[1])):
        return False
    if not (is_vertical_edge(grid, top_left[1], top_left[0], bottom_right[0]) and
            is_vertical_edge(grid, bottom_right[1], top_left[0], bottom_right[0])):
        return False
    return True

def rectangles(strings):
    grid = [list(row) for row in strings]
    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0
    count = 0

    for row1 in range(num_rows):
        for col1 in range(num_cols):
            for row2 in range(row1 + 1, num_rows):
                for col2 in range(col1 + 1, num_cols):
                    if is_rectangle(grid, (row1, col1), (row2, col2)):
                        count += 1

    return count
