def total(basket):
    # Calculate the price of the shopping basket
    # based on the given discount percentages
    unique_books = set(basket)
    total_price = 0

    for num_books in range(1, len(unique_books) + 1):
        price = num_books * 8 * (1 - (num_books - 1) * 0.05)
        total_price += price

    return int(total_price * 100) / 100
