def count_words(sentence):
    word_counts = {}
    words = sentence.lower().split()
    for word in words:
        # Remove punctuation and apostrophes
        word = word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
        if word:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    return word_counts
