def square_root(number):
    root = number
    while root * root > number:
        root = (root + number // root) // 2
    return root