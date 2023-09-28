def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False

    check_digit = isbn[-1]
    if check_digit == "X":
        check_digit = 10
    else:
        try:
            check_digit = int(check_digit)
        except ValueError:
            return False

    digits = [int(d) for d in isbn[:-1]]
    result = sum(d * (10 - i) for i, d in enumerate(digits)) % 11

    return result == check_digit
    if len(isbn) != 10:
        return False

    check_digit = isbn[-1]
    if check_digit == "X":
        check_digit = 10
    else:
        try:
            check_digit = int(check_digit)
        except ValueError:
            return False

    digits = [int(d) for d in isbn[:-1]]
    result = sum(d * (10 - i) for i, d in enumerate(digits)) % 11

    return result == check_digit
