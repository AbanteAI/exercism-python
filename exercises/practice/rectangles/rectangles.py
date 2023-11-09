def rectangles(strings):
    def is_corner(r, c):
        return strings[r][c] == '+'

def is_horizontal_side(r, c1, c2):
    return all(strings[r][c] in '-+' for c in range(c1 + 1, c2))

def is_vertical_side(c, r1, r2):
    return all(strings[r][c] in '|+' for r in range(r1 + 1, r2))

def is_valid_rectangle(top_left, bottom_right):
    top_right = (top_left[0], bottom_right[1])
    bottom_left = (bottom_right[0], top_left[1])
    if not (is_corner(*top_left) and is_corner(*top_right) and
            is_corner(*bottom_left) and is_corner(*bottom_right)):
        return False
    if not (is_horizontal_side(top_left[0], top_left[1], bottom_right[1]) and
            is_horizontal_side(bottom_right[0], top_left[1], bottom_right[1])):
        return False
    if not (is_vertical_side(top_left[1], top_left[0], bottom_right[0]) and
            is_vertical_side(bottom_right[1], top_left[0], bottom_right[0])):
        return False
    return True

    height = len(strings)
    width = len(strings[0]) if height > 0 else 0
    corners = [(r, c) for r in range(height) for c in range(width) if is_corner(r, c)]
    rectangle_count = 0

    for i, top_left in enumerate(corners):
        for bottom_right in corners[i + 1:]:
            if bottom_right[0] > top_left[0] and bottom_right[1] > top_left[1]:
                if is_valid_rectangle(top_left, bottom_right):
                    rectangle_count += 1

    return rectangle_count
