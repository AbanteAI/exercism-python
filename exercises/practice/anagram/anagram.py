def find_anagrams(word, candidates):
    word_lower = word.lower()
    sorted_word = sorted(word_lower)

    def is_anagram(candidate):
        candidate_lower = candidate.lower()
        return (
            word_lower != candidate_lower
            and sorted_word == sorted(candidate_lower)
        )

    return [candidate for candidate in candidates if is_anagram(candidate)]