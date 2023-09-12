def is_valid_triangle(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a
def equilateral(sides):
    return len(set(sides)) == 1 and all(side > 0 for side in sides)

def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    return len(set(sides)) <= 2

def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    return len(set(sides)) == 3