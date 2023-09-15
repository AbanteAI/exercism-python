def rectangles(strings):
    pass
def find_corners(strings):
    corners = []
    for i, row in enumerate(strings):
        for j, char in enumerate(row):
            if char == '+':
                corners.append((i, j))
    return corners

def count_rectangles_between(c1, c2, strings):
    if c1[0] >= c2[0] or c1[1] >= c2[1]:
        return 0

    for i in range(c1[0] + 1, c2[0]):
        if strings[i][c1[1]] not in "|+" or strings[i][c2[1]] not in "|+":
            return 0

    for j in range(c1[1] + 1, c2[1]):
        if strings[c1[0]][j] not in "-+" or strings[c2[0]][j] not in "-+":
            return 0

    return 1

def rectangles(strings):
    corners = find_corners(strings)
    count = 0
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            count += count_rectangles_between(corners[i], corners[j], strings)
    return count
