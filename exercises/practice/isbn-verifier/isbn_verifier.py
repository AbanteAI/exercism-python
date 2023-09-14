def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False

    total = 0
    for i, char in enumerate(isbn):
        if char.isdigit():
            total += int(char) * (10 - i)
        elif char == 'X' and i == 9:
            total += 10
        else:
            return False

    return total % 11 == 0