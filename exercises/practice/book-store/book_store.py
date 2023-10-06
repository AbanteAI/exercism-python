from itertools import combinations

def calculate_price(groups):
    prices = {1: 8, 2: 15.2, 3: 21.6, 4: 25.6, 5: 30}
    prices = {1: 800, 2: 1520, 3: 2160, 4: 2560, 5: 3000}

def total(basket):
    unique_books = set(basket)
    max_discount = float('inf')

    for i in range(1, len(unique_books) + 1):
        for group_combination in combinations(unique_books, i):
            remaining_basket = basket[:]
            groups = []

            for book in group_combination:
                remaining_basket.remove(book)
                groups.append([book])

            for book in remaining_basket:
                min_group = min(groups, key=lambda x: (len(x), x.count(book)))
                min_group.append(book)

            price = calculate_price(groups)
            max_discount = min(max_discount, price)

    return max_discount if max_discount != float('inf') else 0