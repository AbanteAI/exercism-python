def find_anagrams(word, candidates):
    def sorted_letters(w):
        return sorted(w.lower())

    word_sorted = sorted_letters(word)
    anagrams = [candidate for candidate in candidates if sorted_letters(candidate) == word_sorted and candidate.lower() != word.lower()]
    
    return anagrams
