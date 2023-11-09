def _is_valid_triangle(sides):
    a, b, c = sides
    return all(side > 0 for side in sides) and (a + b >= c) and (a + c >= b) and (b + c >= a)
def equilateral(sides):
    return _is_valid_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return _is_valid_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    return _is_valid_triangle(sides) and len(set(sides)) == 3
