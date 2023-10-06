def count_words(sentence):
    words = sentence.lower().split()
    word_count = {}
    for word in words:
        word = word.strip(',:!?')
        if word.startswith("'") and word.endswith("'"):
            word = word.strip("'")
        if word.isdigit() or len(word) == 0:
            continue
        word_count[word] = word_count.get(word, 0) + 1
    return word_count