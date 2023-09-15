import string
def is_pangram(sentence):
    alphabet_set = set(string.ascii_lowercase)
    sentence_set = set(sentence.lower())

    return alphabet_set.issubset(sentence_set)
    pass
