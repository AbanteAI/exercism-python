def rectangles(strings):
    pass
def count_corners(strings, row, col):
    corners = 0
    if strings[row][col] == '+':
        if row > 0 and strings[row - 1][col] == '|':
            corners += 1
        if col > 0 and strings[row][col - 1] == '-':
            corners += 1
        if row < len(strings) - 1 and strings[row + 1][col] == '|':
            corners += 1
        if col < len(strings[row]) - 1 and strings[row][col + 1] == '-':
            corners += 1
    return corners

def is_rectangle(strings, r1, c1, r2, c2):
    if r1 == r2 or c1 == c2:
        return False
    for row in range(r1, r2 + 1):
        if strings[row][c1] != '+' and strings[row][c1] != '|':
            return False
        if strings[row][c2] != '+' and strings[row][c2] != '|':
            return False
    for col in range(c1, c2 + 1):
        if strings[r1][col] != '+' and strings[r1][col] != '-':
            return False
        if strings[r2][col] != '+' and strings[r2][col] != '-':
            return False
    return True

def rectangles(strings):
    count = 0
    for r1 in range(len(strings)):
        for c1 in range(len(strings[r1])):
            if count_corners(strings, r1, c1) >= 2:
                for r2 in range(r1 + 1, len(strings)):
                    for c2 in range(c1 + 1, len(strings[r2])):
                        if is_rectangle(strings, r1, c1, r2, c2):
                            count += 1
    return count
