def square_root(number):
    if number < 0:
        raise ValueError("The radicand must be a positive integer.")
    if number == 0 or number == 1:
        return number
    guess = number / 2
    while True:
        new_guess = (guess + (number / guess)) / 2
        if abs(new_guess - guess) < 1e-10:
            return int(new_guess)
        guess = new_guess