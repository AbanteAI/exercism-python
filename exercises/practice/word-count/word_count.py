import re
from collections import Counter

def count_words(sentence):
    # Normalize to lowercase
    sentence = sentence.lower()
    # Use regex to find words (including contractions), splitting on punctuation and whitespace
    words = re.findall(r"\b\w+(?:'\w+)?\b", sentence)
    # Count the occurrences of each word
    word_count = Counter(words)
    return dict(word_count)
