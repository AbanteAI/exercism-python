def find_anagrams(word, candidates):
    pass
def normalize(word):
    return ''.join(sorted(word.lower()))

def find_anagrams(word, candidates):
    normalized_word = normalize(word)
    return [candidate for candidate in candidates if normalize(candidate) == normalized_word and candidate.lower() != word.lower()]
