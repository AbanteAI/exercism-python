from multiprocessing import Pool
from collections import Counter
import string
def count_letters(text):
    text = text.lower()
    text = ''.join(filter(lambda x: x in string.ascii_lowercase + string.digits, text))
    return Counter(text)

def calculate(text_input):
    with Pool() as pool:
        letter_counts = pool.map(count_letters, text_input)

    result = Counter()
    for letter_count in letter_counts:
        result += letter_count

    return result

    with Pool() as pool:
        letter_counts = pool.map(count_letters, text_input)

    result = Counter()
    for letter_count in letter_counts:
        result += letter_count

    return result
