def total(basket):
    book_counts = [0, 0, 0, 0, 0]
    for book in basket:
        book_counts[book] += 1

    total_price = 0
    while sum(book_counts) > 0:
        distinct_books = sum(1 for count in book_counts if count > 0)
        discount = get_discount(distinct_books)
        total_price += distinct_books * 8 * (1 - discount)

        for i in range(5):
            if book_counts[i] > 0:
                book_counts[i] -= 1

    return total_price

def get_discount(distinct_books):
    discounts = [0, 0, 0.05, 0.1, 0.2, 0.25]
    return discounts[distinct_books]

def get_discount(distinct_books):
    discounts = [0, 0, 0.05, 0.1, 0.2, 0.25]
    return discounts[distinct_books]
