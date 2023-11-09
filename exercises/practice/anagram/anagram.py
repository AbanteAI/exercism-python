def find_anagrams(word, candidates):
    # Normalize the target word for comparison
    normalized_word = sorted(word.lower())
    anagrams = []

    for candidate in candidates:
        # Skip the candidate if it is the same as the word
        if candidate.lower() == word.lower():
            continue
        # Check if the candidate is an anagram of the word
        if sorted(candidate.lower()) == normalized_word:
            anagrams.append(candidate)

    return anagrams
