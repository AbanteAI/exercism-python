def count_words(sentence):
def count_words(sentence):
    words = sentence.lower().split()
    word_counts = {}
    for word in words:
        # Remove punctuation from the word
        word = word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
    words = sentence.lower().split()
    word_counts = {}
    for word in words:
        # Remove punctuation from the word
        word = word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
