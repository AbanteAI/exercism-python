def triangle_inequality(sides):
    a, b, c = sides
    return a + b >= c and b + c >= a and a + c >= b

def equilateral(sides):
    if sides[0] <= 0:
        return False
    return sides[0] == sides[1] == sides[2]

def isosceles(sides):
    if not triangle_inequality(sides):
        return False
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]

def scalene(sides):
    if not triangle_inequality(sides):
        return False
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]
