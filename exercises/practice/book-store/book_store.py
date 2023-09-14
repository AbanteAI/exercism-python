from itertools import combinations
from collections import Counter


def total(basket):
    if not basket:
        return 0

    discount_rates = {1: 1, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}
    book_price = 800

    def price_for_group(group):
        return sum([book_price * discount_rates[len(group)] for group in group])

    def find_groupings(books):
        if not books:
            return [[]]
        groupings = []
        for i in range(1, len(books) + 1):
            for subset in set(combinations(books, i)):
                remaining_books = list(books)
                for book in subset:
                    remaining_books.remove(book)
                groupings.extend([[subset] + group for group in find_groupings(remaining_books)])
        return groupings

    book_counter = Counter(basket)
    books = [book for book, count in book_counter.items() for _ in range(count)]
    all_groupings = find_groupings(books)
    return int(min(price_for_group(group) for group in all_groupings))