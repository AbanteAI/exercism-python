def find_anagrams(word, candidates):
    anagrams = []
    target = word.lower()
    for candidate in candidates:
        if candidate.lower() != target and sorted(candidate.lower()) == sorted(target):
            anagrams.append(candidate)
    return anagrams
