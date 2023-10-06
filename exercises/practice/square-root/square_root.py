def square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    if number == 0:
        return 0

    guess = number / 2
    while True:
        new_guess = (guess + number / guess) / 2
        if abs(new_guess - guess) < 1e-9:
            return new_guess
        guess = new_guess
