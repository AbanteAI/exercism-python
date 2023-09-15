from collections import Counter
from multiprocessing import Pool

def calculate(text_input):
    def count_letters(text):
        return Counter(text)

    with Pool() as pool:
        results = pool.map(count_letters, text_input)

    total_frequency = Counter()
    for result in results:
        total_frequency += result

    return total_frequency
