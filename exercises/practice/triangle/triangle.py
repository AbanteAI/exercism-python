def equilateral(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a == b == c and (a + b >= c) and (b + c >= a) and (a + c >= b)


def isosceles(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a == b or b == c or a == c) and (a + b >= c) and (b + c >= a) and (a + c >= b)


def scalene(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a != b and b != c and a != c and (a + b >= c) and (b + c >= a) and (a + c >= b)
