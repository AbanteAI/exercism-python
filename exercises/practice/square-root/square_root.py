def square_root(number):
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    if number == 0:
        return 0
    guess = number
    while True:
        next_guess = (guess + number / guess) / 2
        if abs(guess - next_guess) < 1e-10:
            return int(next_guess)
        guess = next_guess
