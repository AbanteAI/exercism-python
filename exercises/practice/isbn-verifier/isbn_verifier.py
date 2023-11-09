def is_valid(isbn):
    # Remove hyphens from the ISBN
    isbn = isbn.replace('-', '')
    
    # Validate the length of the ISBN
    if len(isbn) != 10:
        return False
    
    # Check if the first 9 characters are digits and the last character is either a digit or 'X'
    if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
        return False
    
    # Calculate the checksum using the provided formula
    total = 0
    for i, char in enumerate(isbn):
        if char == 'X':
            total += 10 * (10 - i)
        else:
            total += int(char) * (10 - i)
    
    # Return True if the checksum modulo 11 is 0, otherwise return False
    return total % 11 == 0
