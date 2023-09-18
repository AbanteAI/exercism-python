def equilateral(sides):
    if len(set(sides)) == 1 and all(side > 0 for side in sides) and sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        return True
    return False
        return True
    return False
        return True
    return False
def isosceles(sides):
    if len(set(sides)) <= 2 and all(side > 0 for side in sides) and sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        return True
    return False
def isosceles(sides):
    if len(set(sides)) <= 2 and all(side > 0 for side in sides) and sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        return True
    return False
def scalene(sides):
    if len(set(sides)) == 3 and all(side > 0 for side in sides) and sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        return True
    return False


def scalene(sides):
    if len(set(sides)) == 3 and all(side > 0 for side in sides) and sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        return True
    return False
        return True
    return False
