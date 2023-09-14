import re

def count_words(sentence):
    words = re.findall(r"\b\w[\w']*\b", sentence.lower())
    return {word: words.count(word) for word in set(words)}