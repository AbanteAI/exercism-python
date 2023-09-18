def find_anagrams(word, candidates):
    target_word = word.lower()
    sorted_target_word = sorted(target_word)
    anagrams = []

    for candidate in candidates:
        candidate_lower = candidate.lower()
        if candidate_lower != target_word and sorted(candidate_lower) == sorted_target_word:
            anagrams.append(candidate)

    return anagrams