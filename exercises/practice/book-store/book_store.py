def total(basket):
    def calculate_price(groups):
        prices = {1: 800, 2: 1520, 3: 2160, 4: 2560, 5: 3000}
        return sum(prices[len(group)] for group in groups)

    def find_best_discount(books, groups, memo):
        if not books:
            return calculate_price(groups)
        if tuple(books) in memo:
            return memo[tuple(books)]

        min_price = float("inf")
        for group in groups:
            if books[0] not in group:
                group.add(books[0])
                min_price = min(min_price, find_best_discount(books[1:], groups, memo))
                group.remove(books[0])
        new_group = {books[0]}
        groups.append(new_group)
        min_price = min(min_price, find_best_discount(books[1:], groups, memo))
        groups.remove(new_group)

        memo[tuple(books)] = min_price
        return min_price

    if not basket:
        return 0

    basket.sort()
    return find_best_discount(basket, [], {})
    return find_best_discount(basket, [], {})