def is_pangram(sentence):
    letters = set()
    for char in sentence:
        if char.isalpha():
            letters.add(char.lower())
    return len(letters) == 26
