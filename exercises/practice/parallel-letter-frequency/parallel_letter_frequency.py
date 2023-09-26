from collections import Counter
from concurrent.futures import ThreadPoolExecutor


def calculate(text_input):
    def count_letters(text):
        return Counter(filter(str.isalpha, text.lower()))

    with ThreadPoolExecutor() as executor:
        letter_counts = executor.map(count_letters, text_input)

    return sum(letter_counts, Counter())
