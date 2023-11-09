def is_valid(isbn):
    # Remove hyphens from the ISBN
    isbn = isbn.replace('-', '')
    
    # Check if the ISBN length is 10 and the first 9 characters are digits and the last is a digit or 'X'
    if len(isbn) != 10 or not isbn[:-1].isdigit() or (isbn[-1] != 'X' and not isbn[-1].isdigit()):
        return False
    
    # Calculate the checksum using the provided formula
    total = 0
    for i, char in enumerate(isbn):
        if char == 'X':
            total += 10 * (10 - i)
        else:
            total += int(char) * (10 - i)
    
    # Check if the checksum modulo 11 is 0
    return total % 11 == 0
