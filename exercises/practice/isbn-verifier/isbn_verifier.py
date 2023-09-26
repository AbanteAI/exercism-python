def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False

    checksum = 0
    for i, digit in enumerate(isbn):
        if digit == "X" and i == 9:
            checksum += 10
        elif digit.isdigit():
            checksum += int(digit) * (10 - i)
        else:
            return False

    return checksum % 11 == 0
