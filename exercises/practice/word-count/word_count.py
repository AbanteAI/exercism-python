import re
from collections import Counter

def count_words(sentence):
    # Normalize case and remove unwanted punctuation
    normalized_sentence = sentence.lower()
    words = re.findall(r"\b[\w']+\b", normalized_sentence.replace('_', ' '))
    # Count the words using Counter from collections
    word_count = Counter(words)
    return dict(word_count)