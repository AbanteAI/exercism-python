from collections import Counter
from itertools import permutations

def total(basket):
    if not basket:
        return 0

    book_price = 800  # Price in cents
    discounts = {1: 1, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}

    def calculate_price(basket):
        counter = Counter(basket)
        price = 0
        while counter:
            group = set()
            for book in counter:
                if book not in group:
                    group.add(book)
                    counter[book] -= 1
                    if counter[book] == 0:
                        del counter[book]
            price += len(group) * book_price * discounts[len(group)]
        return price

    # Try all permutations of the basket to find the cheapest price
    cheapest_price = float('inf')
    for perm in permutations(sorted(basket)):
        cheapest_price = min(cheapest_price, calculate_price(list(perm)))

    return cheapest_price
