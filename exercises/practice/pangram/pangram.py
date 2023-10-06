def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence = sentence.lower()
    for char in sentence:
        if char.isalpha():
            alphabet.discard(char)
    return len(alphabet) == 0