from collections import Counter
def calculate(text_input):
    letter_count = Counter()
    for line in text_input:
        letter_count.update([char.lower() for char in line if char.isalpha()])
    return dict(letter_count)