def equilateral(sides):
    if 0 in sides:
        return False


def isosceles(sides):
    sorted_sides = sorted(sides)
    return sorted_sides[0] + sorted_sides[1] >= sorted_sides[2]


def scalene(sides):
    sorted_sides = sorted(sides)
    return sorted_sides[0] + sorted_sides[1] >= sorted_sides[2]
