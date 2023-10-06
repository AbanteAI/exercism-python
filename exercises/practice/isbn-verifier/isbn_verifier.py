def is_valid(isbn):
    digits = isbn.replace('-', '')
    if len(digits) != 10:
        return False
    try:
        check_digit = int(digits[-1])
        if check_digit == 'X':
            check_digit = 10
        else:
            check_digit = int(check_digit)
    except ValueError:
        return False
    if not digits[:-1].isdigit():
        return False
    return sum(int(digit) * weight for digit, weight in zip(digits[:-1], range(10, 0, -1))) % 11 == 0
