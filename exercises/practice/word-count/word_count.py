import re
from collections import Counter

def count_words(sentence):
    # Normalize to lowercase
    sentence = sentence.lower()
    # Use regex to find words, considering contractions as single words
    words = re.findall(r"\b[\w']+?\b", sentence.replace('_', ' '))
    # Count the occurrences of each word
    word_count = Counter(words)
    return dict(word_count)
