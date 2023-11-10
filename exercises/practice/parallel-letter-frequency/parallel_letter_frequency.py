from collections import Counter
from concurrent.futures import ThreadPoolExecutor

def calculate(text_input):
    def count_letters(text):
        return Counter(c for c in text.lower() if c.isalpha())

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(count_letters, text) for text in text_input]
        total_count = Counter()
        for future in futures:
            total_count.update(future.result())
    return total_count