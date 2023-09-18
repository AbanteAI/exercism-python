def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10 or not isbn[:9].isdigit() or not (isbn[-1].isdigit() or isbn[-1] == 'X'):
        return False

    check_digit = sum((10 - i) * (int(digit) if digit != 'X' else 10) for i, digit in enumerate(isbn)) % 11
    return check_digit == 0