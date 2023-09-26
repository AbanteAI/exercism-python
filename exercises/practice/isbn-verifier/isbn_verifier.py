def is_valid(isbn):
    isbn = isbn.replace('-', '')  # Remove dashes from the input

    if len(isbn) != 10:
        return False

    if not isbn[:-1].isdigit() or (isbn[-1] != 'X' and not isbn[-1].isdigit()):
        return False

    check_sum = sum((int(digit) if digit.isdigit() else 10) * weight
                    for digit, weight in zip(isbn, range(10, 0, -1)))

    return check_sum % 11 == 0