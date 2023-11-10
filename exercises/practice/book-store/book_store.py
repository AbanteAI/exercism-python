def total(basket):
    # Define the cost of one book and the discount rates
    book_cost = 800  # Cost in cents
    discounts = {1: 1, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}

    # Calculate the price for a given set of books applying the appropriate discount
    def calculate_set_price(num_books):
        return int(num_books * book_cost * discounts[num_books])

    # Calculate the total price with the maximum discount
    def calculate_total(basket):
        # Sort the basket to count each book
        sorted_basket = sorted(basket)
        unique_books = set(sorted_basket)
        total_price = 0

        # While there are still books in the basket
        while sorted_basket:
            # Find the largest set of unique books
            book_set = set()
            for book in unique_books:
                if book in sorted_basket:
                    book_set.add(book)
                    sorted_basket.remove(book)

            # Apply discount to the set and add to the total price
            total_price += calculate_set_price(len(book_set))

            # Update the set of unique books
            unique_books = set(sorted_basket)

        return total_price

    # Return the total price of the basket
    return calculate_total(basket)