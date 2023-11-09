import re
from collections import Counter

def count_words(sentence):
    # Normalize to lowercase
    sentence = sentence.lower()
    # Use regex to split the sentence into words, accounting for contractions
    words = re.findall(r"(?:\w+['\w]*)", sentence)
    # Count the occurrences of each word
    word_count = Counter(words)
    return dict(word_count)
