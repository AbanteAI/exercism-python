def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False

    total = 0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        total += int(isbn[i]) * (10 - i)

    if isbn[-1] == 'X':
        total += 10
    elif isbn[-1].isdigit():
        total += int(isbn[-1])
    else:
        return False

    return total % 11 == 0
