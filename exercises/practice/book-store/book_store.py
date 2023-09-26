def total(basket):
    book_prices = {
        1: 8,
        2: 8,
        3: 8,
        4: 8,
        5: 8
    }
    book_counts = [0, 0, 0, 0, 0]
    for book in basket:
        book_counts[book - 1] += 1

    total_price = 0
    while sum(book_counts) > 0:
        unique_books = sum([1 for count in book_counts if count > 0])
        discount = get_discount(unique_books)
        total_price += (unique_books * (8 - (8 * discount / 100)))
        for i in range(len(book_counts)):
            if book_counts[i] > 0:
                book_counts[i] -= 1
    return round(total_price * 100) / 100


def get_discount(unique_books):
    discounts = {
        1: 0,
        2: 5,
        3: 10,
        4: 20,
        5: 25
    }
    return discounts[unique_books]