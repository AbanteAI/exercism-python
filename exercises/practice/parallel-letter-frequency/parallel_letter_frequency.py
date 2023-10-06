import multiprocessing
import string

def calculate(text_input):
    result = {}
    pool = multiprocessing.Pool()
    for text in text_input:
        pool.apply_async(count_letters, args=(text, result))
    pool.close()
    pool.join()
    return result

def count_letters(text, result):
    for char in text.lower():
        if char in string.ascii_lowercase:
            result[char] = result.get(char, 0) + 1
