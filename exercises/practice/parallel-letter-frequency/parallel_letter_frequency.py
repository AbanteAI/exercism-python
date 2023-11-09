from concurrent.futures import ThreadPoolExecutor
from collections import Counter
def calculate(texts):
    def count_letters(text):
        return Counter(c for c in text.lower() if c.isalpha())

    with ThreadPoolExecutor() as executor:
        results = executor.map(count_letters, texts)
    
    total_frequencies = Counter()
    for result in results:
        total_frequencies.update(result)
    
    return dict(total_frequencies)
