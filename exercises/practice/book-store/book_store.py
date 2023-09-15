def total(basket):
    pass
def cost_of_set(num_books):
    discounts = {1: 1, 2: 0.95, 3: 0.90, 4: 0.80, 5: 0.75}
    return 8 * num_books * discounts[num_books]


def find_best_price(basket, price=0):
    if not basket:
        return price

    unique_books = set(basket)
    min_price = float('inf')

    for num_books in range(1, len(unique_books) + 1):
        new_basket = basket.copy()
        for book in unique_books:
            new_basket.remove(book)
        new_price = find_best_price(new_basket, price + cost_of_set(num_books))
        min_price = min(min_price, new_price)

    return min_price


def total(basket):
    return find_best_price(basket)
