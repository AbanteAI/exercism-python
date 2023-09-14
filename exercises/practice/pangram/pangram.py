from string import ascii_lowercase
def is_pangram(sentence):
    ALPHABET = set(ascii_lowercase)
    return ALPHABET.issubset(sentence.lower())