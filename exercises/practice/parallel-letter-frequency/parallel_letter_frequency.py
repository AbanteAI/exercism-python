from concurrent.futures import ThreadPoolExecutor
from collections import Counter
def count_letters(text):
    return Counter(c for c in text.lower() if c.isalpha())

def calculate(text_input):
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(count_letters, text) for text in text_input]
        total_counts = Counter()
        for future in as_completed(futures):
            total_counts.update(future.result())
    return total_counts
