def is_triangle(sides):
    a, b, c = sides
    return all(side > 0 for side in sides) and (a + b >= c) and (a + c >= b) and (b + c >= a)
def equilateral(sides):
    if not is_triangle(sides):
        return False
    return len(set(sides)) == 1


def isosceles(sides):
    if not is_triangle(sides):
        return False
    return len(set(sides)) <= 2


def scalene(sides):
    if not is_triangle(sides):
        return False
    return len(set(sides)) == 3
