from collections import Counter
def calculate(text_input):
    letter_count = Counter()
    for line in text_input:
        letter_count.update(c.lower() for c in line if c.isalpha())
    return dict(letter_count)