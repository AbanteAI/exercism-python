def find_anagrams(word, candidates):
    word_lower = word.lower()
    word_sorted = sorted(word_lower)
    return [
        candidate
        for candidate in candidates
        if sorted(candidate.lower()) == word_sorted and candidate.lower() != word_lower
    ]