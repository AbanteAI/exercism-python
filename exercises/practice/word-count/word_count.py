import re
from collections import Counter

def count_words(sentence):
def count_words(sentence):
    # Use regex to find words, considering contractions as single words
    # Update regex to treat underscores and other non-alphanumerics as separators
    words = re.findall(r"\b[\w'-]+(?<!_)\b", re.sub(r'[_\W]+', ' ', sentence))
    
    # Convert all words to lowercase and count occurrences
    word_counts = Counter(word.lower() for word in words if word)
    
    return dict(word_counts)