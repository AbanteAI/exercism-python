import concurrent.futures
def calculate(text_input):
    total_frequency = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(count_letters, text_input)
        for result in results:
            for letter, count in result.items():
                total_frequency[letter] = total_frequency.get(letter, 0) + count
    return total_frequency

def count_letters(text):
    frequency = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            frequency[letter] = frequency.get(letter, 0) + 1
    return frequency