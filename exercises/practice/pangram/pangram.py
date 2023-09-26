def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence = sentence.lower()
    return all(letter in sentence for letter in alphabet)
