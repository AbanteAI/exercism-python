def is_valid(isbn):
    # Remove hyphens
    isbn = isbn.replace("-", "")
    
    # Validate length of the ISBN
    if len(isbn) != 10:
        return False
    
    # Validate ISBN format: first 9 characters should be digits and the last character should be a digit or 'X'
    if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == "X")):
        return False
    
    # Calculate the checksum using the provided formula
    total = 0
    for i, char in enumerate(isbn):
        if char == 'X':
            total += 10 * (10 - i)
        else:
            total += int(char) * (10 - i)
    
    # Check if the checksum is valid
    return total % 11 == 0
