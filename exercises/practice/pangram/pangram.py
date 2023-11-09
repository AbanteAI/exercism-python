def is_pangram(sentence):
    """
    Check if a sentence is a pangram.

    A pangram is a sentence using every letter of the alphabet at least once.
    This function is case insensitive.

    :param sentence: The sentence to check.
    :return: True if the sentence is a pangram, False otherwise.
    """
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(sentence.lower())
