def rectangles(strings):
    pass
def find_corners(strings):
    corners = []
    for i, row in enumerate(strings):
        for j, char in enumerate(row):
            if char == '+':
                corners.append((i, j))
    return corners

def is_rectangle(strings, top_left, top_right, bottom_left, bottom_right):
    if strings[top_left[0]][top_right[1]] == '+' and strings[bottom_left[0]][bottom_right[1]] == '+':
        for i in range(top_left[1] + 1, top_right[1]):
            if strings[top_left[0]][i] != '-' or strings[bottom_left[0]][i] != '-':
                return False
        for i in range(top_left[0] + 1, bottom_left[0]):
            if strings[i][top_left[1]] != '|' or strings[i][top_right[1]] != '|':
                return False
        return True
    return False

def rectangles(strings):
    corners = find_corners(strings)
    count = 0
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            for k in range(j + 1, len(corners)):
                for l in range(k + 1, len(corners)):
                    if is_rectangle(strings, corners[i], corners[j], corners[k], corners[l]):
                        count += 1
    return count
