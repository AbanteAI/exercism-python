from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import string
def calculate(text_input):
    def count_letters(text):
        return Counter(letter.lower() for letter in text if letter.lower() in string.ascii_lowercase)

    with ThreadPoolExecutor() as executor:
        letter_counts = executor.map(count_letters, text_input)

    total_counts = Counter()
    for count in letter_counts:
        total_counts += count

    return dict(total_counts)