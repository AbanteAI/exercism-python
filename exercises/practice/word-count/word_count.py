import re
def count_words(sentence):
    words = re.findall(r"\b[\w']+\b", sentence.lower())
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count