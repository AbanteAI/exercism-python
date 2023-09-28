def is_pangram(sentence):
    unique_letters = set(c.lower() for c in sentence if c.isalpha())
    return len(unique_letters) == 26
