def find_anagrams(word, candidates):
    target = word.lower()
    sorted_target = sorted(target)
    return [candidate for candidate in candidates if candidate.lower() != target and sorted(candidate.lower()) == sorted_target]
