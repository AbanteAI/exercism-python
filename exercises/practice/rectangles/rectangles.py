def rectangles(strings):
    def is_corner(x, y):
        return strings[y][x] == '+'

    def is_horizontal_edge(x, y):
        return strings[y][x] == '-'

    def is_vertical_edge(x, y):
        return strings[y][x] == '|'

    def find_corners():
        return [(x, y) for y in range(len(strings)) for x in range(len(strings[y])) if is_corner(x, y)]

    def has_complete_edges(corner1, corner2):
        top, bottom = sorted([corner1[1], corner2[1]])
        left, right = sorted([corner1[0], corner2[0]])
        top_edge = all(is_horizontal_edge(x, top) for x in range(left + 1, right))
        bottom_edge = all(is_horizontal_edge(x, bottom) for x in range(left + 1, right))
        left_edge = all(is_vertical_edge(left, y) for y in range(top + 1, bottom))
        right_edge = all(is_vertical_edge(right, y) for y in range(top + 1, bottom))
        return top_edge and bottom_edge and left_edge and right_edge

    def is_valid_rectangle(corner1, corner2, corner3, corner4):
        return has_complete_edges(corner1, corner2) and has_complete_edges(corner2, corner3) and has_complete_edges(corner3, corner4) and has_complete_edges(corner4, corner1)

    corners = find_corners()
    count = 0
    for i, corner1 in enumerate(corners):
        for j, corner2 in enumerate(corners[i + 1:], start=i + 1):
            if corner1[0] == corner2[0] or corner1[1] == corner2[1]:
                continue
            for k, corner3 in enumerate(corners[j + 1:], start=j + 1):
                if corner3[0] not in [corner1[0], corner2[0]] or corner3[1] not in [corner1[1], corner2[1]]:
                    continue
                for corner4 in corners[k + 1:]:
                    if corner4[0] in [corner1[0], corner2[0]] and corner4[1] in [corner1[1], corner2[1]]:
                        if is_valid_rectangle(corner1, corner2, corner3, corner4):
                            count += 1
    return count
