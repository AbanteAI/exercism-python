def is_valid(isbn):
    isbn = isbn.replace("-", "")  # Remove dashes from the input string

    if len(isbn) != 10:  # Check if the length is valid
        return False

    try:
        digits = [int(char) if char.isdigit() else 10 if char.upper() == 'X' else None for char in isbn]  # Convert digits to integers, 'X' to 10
    except ValueError:
        return False

    return sum((i + 1) * digit for i, digit in enumerate(digits) if digit is not None) % 11 == 0  # Check if the sum is divisible by 11
