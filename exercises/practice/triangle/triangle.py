def equilateral(sides):
    a, b, c = sides
    return a == b == c and a > 0


def isosceles(sides):
    return (a == b or a == c or b == c) and a + b > c and a + c > b and b + c > a
    return (a == b or a == c or b == c) and a + b >= c and a + c >= b and b + c >= a


def scalene(sides):
    return a != b != c and a + b > c and a + c > b and b + c > a
    return a != b != c and a + b >= c and a + c >= b and b + c >= a
