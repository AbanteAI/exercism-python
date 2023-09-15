import re
def is_valid(isbn):
    if not re.match(r'^(?:\d-?){9}(?:\d|X)(?:-)?$', isbn):
        return False
    isbn = re.sub(r'[^0-9X]', '', isbn)

    checksum = sum((10 - i) * (int(c) if c != 'X' else 10) for i, c in enumerate(isbn)) % 11

    return checksum == 0
