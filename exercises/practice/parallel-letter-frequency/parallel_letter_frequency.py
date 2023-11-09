from collections import Counter
from concurrent.futures import ThreadPoolExecutor
def calculate(text_input):
    def count_letters(text):
        return Counter(c.lower() for c in text if c.isalpha())

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(count_letters, text) for text in text_input]
        total_counts = Counter()
        for future in as_completed(futures):
            total_counts.update(future.result())
    return total_counts
