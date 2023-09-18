def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence = sentence.lower()
    sentence_letters = set(sentence)
    return alphabet.issubset(sentence_letters)
