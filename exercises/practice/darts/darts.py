def score(x, y):
    """
    Calculate the score of a single toss in a Darts game.

    Parameters:
    x (float): The x-coordinate of the point where the dart landed.
    y (float): The y-coordinate of the point where the dart landed.

    Returns:
    int: The score earned by the dart landing at the point (x, y).
    """
    distance_squared = x**2 + y**2
    if distance_squared <= 1**2:
        return 10
    elif distance_squared <= 5**2:
        return 5
    elif distance_squared <= 10**2:
        return 1
    else:
        return 0
