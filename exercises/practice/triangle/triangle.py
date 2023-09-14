def equilateral(sides):
    a, b, c = sides
    return a != 0 and a == b == c


def isosceles(sides):
    a, b, c = sides
    return (a + b > c) and (a + c > b) and (b + c > a) and (a == b or a == c or b == c)


def scalene(sides):
    a, b, c = sides
    return (a + b > c) and (a + c > b) and (b + c > a) and (a != b and a != c and b != c)
