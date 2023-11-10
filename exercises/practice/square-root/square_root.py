def square_root(number):
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    if number == 0 or number == 1:
        return number
    
    # Using the Babylonian method (also known as Heron's method) for finding square roots
    guess = number / 2
    while True:
        next_guess = (guess + number / guess) / 2
        if abs(next_guess - guess) < 1e-7:  # Precision check
            return int(next_guess)
        guess = next_guess