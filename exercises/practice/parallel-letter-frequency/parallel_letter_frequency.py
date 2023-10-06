from collections import Counter
from multiprocessing import Pool

def calculate(text_input):
    with Pool() as pool:
        results = pool.map(count_letters, text_input)
    return sum(results, Counter())

def count_letters(text):
    return Counter(filter(str.isalpha, text.lower()))
