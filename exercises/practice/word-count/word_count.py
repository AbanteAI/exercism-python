import re
def count_words(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r"[^\w']+", " ", sentence)
    sentence = re.sub(r"[^\w']+|(?<!\w)'|'(?!\w)", " ", sentence)
    sentence = re.sub(r"[^\w']|(?<=\w)'|'(?=\w)", " ", sentence)
    words = sentence.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts