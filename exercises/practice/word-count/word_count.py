import re
def count_words(sentence):
    words = re.findall(r"\b[\w']+\b", sentence)
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
