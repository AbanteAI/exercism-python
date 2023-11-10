def is_valid(isbn):
    # Remove hyphens
    isbn = isbn.replace("-", "")
    
    # Validate length of ISBN
    if len(isbn) != 10:
        return False
    
    # Calculate checksum using the formula
    total = 0
    for i, char in enumerate(isbn):
        if (char.isdigit()):
            total += int(char) * (10 - i)
        elif (char == 'X' and i == 9):
            total += 10
        else:
            return False
    
    # Check if the ISBN is valid
    return total % 11 == 0