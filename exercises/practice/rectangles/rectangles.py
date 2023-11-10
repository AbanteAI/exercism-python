def rectangles(strings):
    def is_corner(x, y):
        return strings[y][x] == '+'

    def is_horizontal_edge(x, y):
        return strings[y][x] == '-'

    def is_vertical_edge(x, y):
        return strings[y][x] == '|'

    def find_corners():
        return [(x, y) for y in range(len(strings)) for x in range(len(strings[y])) if is_corner(x, y)]

    def is_rectangle(corner1, corner2, corner3, corner4):
        # Check if all corners form a rectangle
        if not (is_corner(*corner1) and is_corner(*corner2) and is_corner(*corner3) and is_corner(*corner4)):
            return False
        # Check if the edges between the corners are continuous and valid
        top_edge = all(is_horizontal_edge(x, corner1[1]) for x in range(corner1[0] + 1, corner2[0]))
        bottom_edge = all(is_horizontal_edge(x, corner3[1]) for x in range(corner3[0] + 1, corner4[0]))
        left_edge = all(is_vertical_edge(corner1[0], y) for y in range(corner1[1] + 1, corner3[1]))
        right_edge = all(is_vertical_edge(corner2[0], y) for y in range(corner2[1] + 1, corner4[1]))
        return top_edge and bottom_edge and left_edge and right_edge

    def find_rectangles(corners):
        rectangles = []
        for i in range(len(corners)):
            for j in range(i + 1, len(corners)):
                for k in range(j + 1, len(corners)):
                    for l in range(k + 1, len(corners)):
                        if is_rectangle(corners[i], corners[j], corners[k], corners[l]):
                            rectangles.append((corners[i], corners[j], corners[k], corners[l]))
        return rectangles

    corners = find_corners()
    corners = find_corners()
    rectangles_found = find_rectangles(corners)
    return len(rectangles_found)