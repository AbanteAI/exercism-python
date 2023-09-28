def rectangles(strings):
    pass
def find_corners(strings):
    corners = []
    for i, row in enumerate(strings):
        for j, char in enumerate(row):
            if char == '+':
                corners.append((i, j))
    return corners

def rectangles(strings):
    corners = find_corners(strings)
    count = 0
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            x1, y1 = corners[i]
            x2, y2 = corners[j]
            if x1 < x2 and y1 < y2:
                top_left = all(c in ('+', '-') for c in strings[x1][y1 + 1:y2]) and strings[x1][y1] == '+'
                top_right = all(c in ('+', '-') for c in strings[x2][y1 + 1:y2]) and strings[x2][y1] == '+'
                left = all(c in ('+', '|') for c in (strings[x][y1] for x in range(x1 + 1, x2))) and strings[x1][y2] == '+'
                right = all(c in ('+', '|') for c in (strings[x][y2] for x in range(x1 + 1, x2))) and strings[x2][y2] == '+'
                if top_left and top_right and left and right:
                    count += 1
    return count
