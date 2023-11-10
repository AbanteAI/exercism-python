def equilateral(sides):
    return all(side > 0 for side in sides) and len(set(sides)) == 1


def isosceles(sides):
    return all(side > 0 for side in sides) and (len(set(sides)) == 2 or equilateral(sides)) and valid_triangle(sides)


def scalene(sides):
    return all(side > 0 for side in sides) and len(set(sides)) == 3 and valid_triangle(sides)
def valid_triangle(sides):
    a, b, c = sides
    return a + b >= c and b + c >= a and a + c >= b
