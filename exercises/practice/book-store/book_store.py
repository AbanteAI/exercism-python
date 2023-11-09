def total(basket):
    # Define book price and discount tiers
    book_price = 8
    discounts = {1: 0, 2: 0.05, 3: 0.1, 4: 0.2, 5: 0.25}

    # Function to calculate price for a group of books
    def calculate_group_price(group):
        distinct_books = len(set(group))
        discount = discounts[distinct_books]
        return distinct_books * book_price * (1 - discount)

    # Function to find the best discount for the basket
    def best_discount(basket):
        groups = []

        for book in basket:
            placed = False
            for group in groups:
                if book not in group:
                    group.append(book)
                    placed = True
                    break
            if not placed:
                groups.append([book])

        return sum(calculate_group_price(group) for group in groups)

    # Calculate and return the best possible discount in cents
    return int(best_discount(sorted(basket)) * 100)