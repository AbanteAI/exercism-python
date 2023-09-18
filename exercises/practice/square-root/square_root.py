def square_root(number):
    if number < 0:
        raise ValueError("The radicand must be a natural number.")
    if number == 0 or number == 1:
        return number

    x = number
    y = (x + 1) // 2

    while y < x:
        x = y
        y = (x + number // x) // 2

    return x
