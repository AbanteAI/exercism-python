from concurrent.futures import ThreadPoolExecutor
from collections import Counter
def calculate(text_input):
    def count_letters(text):
        return Counter(c for c in text.lower() if c.isalpha())

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(count_letters, text) for text in text_input]
        total_frequency = Counter()
        for future in as_completed(futures):
            total_frequency.update(future.result())
    return total_frequency
