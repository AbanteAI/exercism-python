def total(basket):
    # Define book price and discount tiers
    book_price = 800  # price in cents
    discounts = {1: 1, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}

    # Function to calculate price for a set of unique books
    def calculate_set_price(num_unique_books):
        return num_unique_books * book_price * discounts[num_unique_books]

    # Function to find the best discount for the basket
    def best_discount(basket):
        sets = []
        for book in basket:
            placed = False
            for set_ in sets:
                if book not in set_:
                    set_.add(book)
                    placed = True
                    break
            if not placed:
                sets.append({book})
        return sum(calculate_set_price(len(set_)) for set_ in sets)

    # Calculate the best price
    best_price = best_discount(basket)

    # Optimize by switching from 5+3 to 4+4 if cheaper
    while True:
        unique_sets = [set_ for set_ in sets if len(set_) == 5]
        if len(unique_sets) < 2:
            break
        set1 = unique_sets[0]
        set2 = unique_sets[1]
        for book in set1:
            if book not in set2:
                set1.remove(book)
                set2.add(book)
                if calculate_set_price(4) * 2 < calculate_set_price(5) + calculate_set_price(3):
                    best_price = best_price - calculate_set_price(5) - calculate_set_price(3) + 2 * calculate_set_price(4)
                else:
                    set1.add(book)
                    set2.remove(book)
                break

    return best_price
