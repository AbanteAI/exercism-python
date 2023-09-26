def total(basket):
    book_prices = {
        1: 8,
        2: 8,
        3: 8,
        4: 8,
        5: 8
    }
    book_discounts = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }
    for book in basket:
        book_discounts[book] += 1
    total_price = 0
    while sum(book_discounts.values()) > 0:
        group_discounts = [0] * 5
        for i, count in enumerate(book_discounts.values()):

            if count > 0:
                group_discounts[i] = 1
                book_discounts[i + 1] -= 1
        group_size = sum(group_discounts)
        group_discount = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        if group_size == 2:
            group_discount = {1: 0.05, 2: 0.05, 3: 0, 4: 0, 5: 0}
        elif group_size == 3:
            group_discount = {1: 0.1, 2: 0.1, 3: 0.1, 4: 0, 5: 0}
        elif group_size == 4:
            group_discount = {1: 0.2, 2: 0.2, 3: 0.2, 4: 0.2, 5: 0}
        elif group_size == 5:
            group_discount = {1: 0.25, 2: 0.25, 3: 0.25, 4: 0.25, 5: 0.25}
        group_price = sum([book_prices[i + 1] * (1 - group_discount[i + 1]) for i in range(5)])
        total_price += group_price
    return total_price
