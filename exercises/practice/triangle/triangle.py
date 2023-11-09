def equilateral(sides):
    return len(set(sides)) == 1 and all(side > 0 for side in sides)


def isosceles(sides):
    return len(set(sides)) <= 2 and all(side > 0 for side in sides) and (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1])


def scalene(sides):
    return len(set(sides)) == 3 and all(side > 0 for side in sides) and (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1])
