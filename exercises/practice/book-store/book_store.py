def total(basket):
def total(basket):
    # Calculate the price of the shopping basket
    # Apply appropriate discounts based on the number of different books
    # Return the total price
    price = 0
    book_counts = {}
    for book in basket:
        book_counts[book] = book_counts.get(book, 0) + 1

    while book_counts:
        distinct_books = len(book_counts)
        discount = get_discount(distinct_books)
        price += distinct_books * 8 * (1 - discount)

        for book in book_counts:
            book_counts[book] -= 1
            if book_counts[book] == 0:
                del book_counts[book]

    return price

def get_discount(distinct_books):
    if distinct_books == 2:
        return 0.05
    elif distinct_books == 3:
        return 0.10
    elif distinct_books == 4:
        return 0.20
    elif distinct_books == 5:
        return 0.25
    else:
        return 0
