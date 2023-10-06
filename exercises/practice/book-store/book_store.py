def total(basket):
    book_counts = [0] * 5
    for book in basket:
        book_counts[book - 1] += 1

    discounts = [0, 0.05, 0.1, 0.2, 0.25]
    total_price = 0
    while any(book_counts):
        distinct_books = sum(1 for count in book_counts if count > 0)
        discount = discounts[min(distinct_books, len(discounts) - 1)]
        total_price += distinct_books * (8 - (8 * discount))
        for i in range(len(book_counts)):
            if book_counts[i] > 0:
                book_counts[i] -= 1

    return total_price

