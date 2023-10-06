import re
import re

def count_words(sentence):
word_list = re.findall(r"\b[\w']+\b", sentence.lower().replace("_", " "))
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count