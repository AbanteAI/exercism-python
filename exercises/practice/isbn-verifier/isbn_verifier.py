def is_valid(isbn):
    # Remove hyphens from the ISBN
    isbn = isbn.replace('-', '')
    
    # Check if the ISBN length is 10 and the first 9 characters are digits and the last is a digit or 'X'
    if len(isbn) != 10 or not isbn[:-1].isdigit() or (isbn[-1] not in '0123456789X'):
        return False
    
    # Calculate the checksum using the ISBN-10 formula
    total = sum((10 - i) * (10 if x == 'X' else int(x)) for i, x in enumerate(isbn))
    
    # Check if the checksum modulo 11 is 0
    return total % 11 == 0