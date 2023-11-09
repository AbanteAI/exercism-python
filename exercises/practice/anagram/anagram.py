def find_anagrams(word, candidates):
    """
    Find anagrams of a given word from a list of candidates.

    Args:
        word (str): The word to find anagrams for.
        candidates (list): A list of candidate words to check against the given word.

    Returns:
        list: A list of anagrams found among the candidates.
    """
    # Normalize the word to lowercase for comparison and sort the letters
    normalized_word = sorted(word.lower())
    anagrams = []

    for candidate in candidates:
        # A word is not an anagram of itself and must be of same length
        if candidate.lower() != word.lower() and len(candidate) == len(word):
            # Check if the candidate is an anagram of the word
            if sorted(candidate.lower()) == normalized_word:
                anagrams.append(candidate)
    
    return anagrams
