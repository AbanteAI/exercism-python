def equilateral(sides):
    return len(set(sides)) == 1 and all(side > 0 for side in sides)


def isosceles(sides):
    a, b, c = sorted(sides)
    return (a + b > c) and (len(set(sides)) <= 2)


def scalene(sides):
    a, b, c = sorted(sides)
    return (a + b > c) and (len(set(sides)) == 3)
