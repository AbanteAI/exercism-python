def count_words(sentence):
    import re
    words = re.findall(r"\b\w+'\w+|\b\w+\b", sentence.lower())
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
