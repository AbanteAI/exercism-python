from itertools import permutations

def total(basket):
    if not basket:
        return 0

    unique_books = len(set(basket))
    if unique_books == 1:
        return 8 * len(basket)

    discounts = [0, 0, 5, 10, 20, 25]
    min_price = float('inf')

    for perm in permutations(discounts[1:unique_books + 1]):
        price = 0
        remaining_books = basket.copy()
        for discount in perm:
            books_to_remove = []
            for book in set(remaining_books):
                books_to_remove.append(book)
                if len(books_to_remove) == discount:
                    break
            for book in books_to_remove:
                remaining_books.remove(book)
                price += 8 * (100 - discounts[len(books_to_remove)]) / 100

        min_price = min(min_price, price)

    return min_price