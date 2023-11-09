def find_anagrams(word, candidates):
    def is_anagram(target, candidate):
        return (sorted(target.lower()) == sorted(candidate.lower()) and
                target.lower() != candidate.lower())

    return [candidate for candidate in candidates if is_anagram(word, candidate)]
