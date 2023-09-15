def is_valid(isbn):
    isbn = isbn.replace("-", "")  # Remove dashes from the string
    if len(isbn) != 10:  # Check if the length is 10
        return False
    check_digit = isbn[-1]  # Get the last character as the check digit
    if check_digit == "X":  # Convert 'X' to 10
        check_digit = 10
    else:
        try:
            check_digit = int(check_digit)  # Convert check digit to integer
        except ValueError:
            return False
    digits = isbn[:-1]  # Get the first 9 digits
    try:
        digits = [int(d) for d in digits]  # Convert digits to integers
    except ValueError:
        return False
    result = sum(d * (10 - i) for i, d in enumerate(digits))  # Calculate the result using the formula
    return result % 11 == check_digit  # Check if the result is valid
