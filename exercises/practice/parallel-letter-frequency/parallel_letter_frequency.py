from concurrent.futures import ThreadPoolExecutor
from collections import Counter
def calculate(text_input):
    def count_letters(text):
        return Counter(char.lower() for char in text if char.isalpha())

    with ThreadPoolExecutor() as executor:
        letter_counts = executor.map(count_letters, text_input)

    total_count = Counter()
    for count in letter_counts:
        total_count += count

    return dict(total_count)