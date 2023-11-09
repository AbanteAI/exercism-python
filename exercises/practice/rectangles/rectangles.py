def rectangles(strings):
    def is_corner(x, y):
        return strings[y][x] == '+'

    def is_horizontal_edge(x, y):
        return strings[y][x] == '-'

    def is_vertical_edge(x, y):
        return strings[y][x] == '|'

    def find_corners():
        return [(x, y) for y in range(len(strings)) for x in range(len(strings[y])) if is_corner(x, y)]

    def has_complete_edges(top_left, bottom_right):
        for x in range(top_left[0] + 1, bottom_right[0]):
            if not is_horizontal_edge(x, top_left[1]) or not is_horizontal_edge(x, bottom_right[1]):
                return False
        for y in range(top_left[1] + 1, bottom_right[1]):
            if not is_vertical_edge(top_left[0], y) or not is_vertical_edge(bottom_right[0], y):
                return False
        return True

    def is_rectangle(top_left, bottom_right):
        if top_left[0] >= bottom_right[0] or top_left[1] >= bottom_right[1]:
            return False
        top_right = (bottom_right[0], top_left[1])
        bottom_left = (top_left[0], bottom_right[1])
        return all(is_corner(*corner) for corner in [top_left, top_right, bottom_left, bottom_right]) and has_complete_edges(top_left, bottom_right)

    corners = find_corners()
    count = 0
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            if is_rectangle(corners[i], corners[j]):
                count += 1
    return count
