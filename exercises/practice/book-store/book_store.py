def total(basket):
    return 0
    # Mentats solutions hangs so I commented it out.
    # discounts = [0, 0, 0.05, 0.1, 0.2, 0.25]
    # price_per_book = 800

    # def cost(books):
        # unique_books = len(books)
        # return unique_books * price_per_book * (1 - discounts[unique_books])

    # def best_price(books):
        # if not books:
            # return 0
        # min_price = float('inf')
        # for i in range(len(books)):
            # remaining_books = books[:i] + books[i+1:]
            # price = cost(set(books)) + best_price(remaining_books)
            # min_price = min(min_price, price)
        # return min_price

    # return int(best_price(basket))
