import re
def count_words(sentence):
    words = re.findall(r"[a-zA-Z0-9]+('[a-zA-Z0-9])*", sentence.lower())
    word_count = {}
    for word in words:
        if word.startswith("'") and word.endswith("'"):
            word = word[1:-1]
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
