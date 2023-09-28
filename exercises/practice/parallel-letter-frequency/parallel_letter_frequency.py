from collections import Counter
from multiprocessing import Pool

def calculate(text_input):
    def count_letters(text):
        return Counter(text.lower())

    with Pool() as pool:
        results = pool.map(count_letters, text_input)

    total_frequency = sum(results, Counter())
    return total_frequency
    def count_letters(text):
        return Counter(text.lower())

    with Pool() as pool:
        results = pool.map(count_letters, text_input)

    total_frequency = sum(results, Counter())
    return total_frequency
